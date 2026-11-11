import pygame
import random
import sys

# ---------------------------------------------------------
# CONSTANTS & CONFIGURATION
# ---------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_FPS = 60

# Native Color objects
COLOR_BLACK = pygame.Color(10, 10, 15)
COLOR_WHITE = pygame.Color(240, 240, 250)
COLOR_GREEN = pygame.Color(0, 255, 140)
COLOR_RED = pygame.Color(255, 70, 70)
COLOR_YELLOW = pygame.Color(255, 215, 0)
COLOR_CYAN = pygame.Color(0, 225, 255)
COLOR_PURPLE = pygame.Color(190, 80, 255)

# ---------------------------------------------------------
# PROCEDURAL GRAPHICS (Using pygame-ce antialiased primitives)
# ---------------------------------------------------------
def create_player_surf():
    surf = pygame.Surface((44, 26), pygame.SRCALPHA)
    # Gun nozzle
    pygame.draw.rect(surf, COLOR_GREEN, (20, 0, 4, 8))
    # Body hull using polygon
    pygame.draw.polygon(surf, COLOR_GREEN, [(6, 26), (22, 6), (38, 26)])
    # Wing extensions
    pygame.draw.rect(surf, COLOR_GREEN, (0, 16, 44, 10), border_radius=2)
    return surf

def create_alien_surf(color: pygame.Color):
    surf = pygame.Surface((34, 26), pygame.SRCALPHA)
    # Chassis
    pygame.draw.rect(surf, color, (6, 5, 22, 14), border_radius=4)
    # Antennae
    pygame.draw.aaline(surf, color, (8, 5), (3, 0))
    pygame.draw.aaline(surf, color, (25, 5), (30, 0))
    # Base appendages
    pygame.draw.rect(surf, color, (4, 19, 6, 7), border_radius=1)
    pygame.draw.rect(surf, color, (24, 19, 6, 7), border_radius=1)
    pygame.draw.rect(surf, color, (14, 19, 6, 4))
    # Cutout eyes
    pygame.draw.rect(surf, COLOR_BLACK, (10, 9, 4, 4))
    pygame.draw.rect(surf, COLOR_BLACK, (20, 9, 4, 4))
    return surf

# ---------------------------------------------------------
# SPRITE CLASSES (Utilizing FRect & Vector2)
# ---------------------------------------------------------
class Laser(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, speed_y: float, color: pygame.Color):
        super().__init__()
        self.image = pygame.Surface((4, 14), pygame.SRCALPHA)
        self.image.fill(color)
        
        # FRect provides sub-pixel floating-point position tracking
        self.rect = pygame.FRect(0, 0, 4, 14)
        self.rect.center = (x, y)
        self.velocity = pygame.Vector2(0, speed_y)

    def update(self, dt: float):
        # Frame-rate independent translation
        self.rect.center += self.velocity * dt
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = create_player_surf()
        self.rect = pygame.FRect(self.image.get_rect())
        self.rect.midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30)
        
        self.speed = 360.0  # Pixels per second
        self.shoot_cooldown = 0.28  # Seconds
        self.cooldown_timer = 0.0

    def update(self, dt: float, keys):
        # Update shooting timer
        if self.cooldown_timer > 0.0:
            self.cooldown_timer -= dt

        move_direction = 0.0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            move_direction -= 1.0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            move_direction += 1.0

        self.rect.x += move_direction * self.speed * dt
        # Clamp FRect strictly within display boundary
        self.rect.clamp_ip(pygame.FRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    def can_shoot(self) -> bool:
        return self.cooldown_timer <= 0.0

    def shoot(self, laser_group: pygame.sprite.Group):
        if self.can_shoot():
            self.cooldown_timer = self.shoot_cooldown
            laser = Laser(self.rect.centerx, self.rect.top, -540.0, COLOR_GREEN)
            laser_group.add(laser)

class Alien(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, row: int):
        super().__init__()
        self.row = row
        if row == 0:
            self.points = 30
            self.image = create_alien_surf(COLOR_PURPLE)
        elif row in (1, 2):
            self.points = 20
            self.image = create_alien_surf(COLOR_CYAN)
        else:
            self.points = 10
            self.image = create_alien_surf(COLOR_YELLOW)

        self.rect = pygame.FRect(self.image.get_rect(topleft=(x, y)))

# ---------------------------------------------------------
# MAIN GAME LOOP
# ---------------------------------------------------------
class SpaceInvaders:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Invaders (pygame-ce)")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        # System font rendering
        self.font = pygame.font.SysFont("monospace", 22, bold=True)
        self.title_font = pygame.font.SysFont("monospace", 44, bold=True)

        # Starfield using Vector2 for positions and speeds
        self.stars = [
            {
                "pos": pygame.Vector2(random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT)),
                "speed": random.choice([25.0, 50.0, 90.0]),
                "radius": 1 if random.random() < 0.75 else 2
            }
            for _ in range(80)
        ]

        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.lives = 3
        self.game_state = "PLAYING"

        self.player = Player()
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.player_lasers = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.alien_direction = 1.0
        self.base_alien_speed = 60.0  # Pixels per second
        self.alien_drop_distance = 18.0
        self.alien_fire_cooldown = 0.85
        self.alien_fire_timer = 0.0

        self.spawn_fleet()

    def spawn_fleet(self):
        rows = 5
        cols = 10
        x_spacing = 56.0
        y_spacing = 42.0
        x_start = (SCREEN_WIDTH - (cols * x_spacing)) / 2.0
        y_start = 65.0

        for r in range(rows):
            for c in range(cols):
                alien = Alien(x_start + c * x_spacing, y_start + r * y_spacing, r)
                self.aliens.add(alien)
        self.total_aliens = len(self.aliens)

    def update_fleet(self, dt: float):
        remaining = len(self.aliens)
        if remaining == 0:
            self.game_state = "VICTORY"
            return

        # Ratio acceleration as count decreases
        ratio_cleared = 1.0 - (remaining / self.total_aliens)
        speed = (self.base_alien_speed + (ratio_cleared * 150.0)) * dt

        shift_down = False
        dx = self.alien_direction * speed

        for alien in self.aliens:
            alien.rect.x += dx
            if alien.rect.right >= SCREEN_WIDTH - 15 or alien.rect.left <= 15:
                shift_down = True

        if shift_down:
            self.alien_direction *= -1.0
            for alien in self.aliens:
                alien.rect.y += self.alien_drop_distance
                if alien.rect.bottom >= self.player.rect.top:
                    self.game_state = "GAMEOVER"

    def handle_alien_fire(self, dt: float):
        self.alien_fire_timer += dt
        if self.alien_fire_timer >= self.alien_fire_cooldown and self.aliens:
            self.alien_fire_timer = 0.0

            # Find the bottom-most alien in each active column
            columns = {}
            for alien in self.aliens:
                col_key = round(alien.rect.x / 10.0) * 10
                if col_key not in columns or alien.rect.y > columns[col_key].rect.y:
                    columns[col_key] = alien

            shooter = random.choice(list(columns.values()))
            laser = Laser(shooter.rect.centerx, shooter.rect.bottom, 320.0, COLOR_RED)
            self.alien_lasers.add(laser)

    def check_collisions(self):
        # groupcollide handles FRect overlap with sub-pixel precision
        hits = pygame.sprite.groupcollide(self.player_lasers, self.aliens, True, True)
        for _, hit_aliens in hits.items():
            for alien in hit_aliens:
                self.score += alien.points

        if pygame.sprite.spritecollide(self.player, self.alien_lasers, True):
            self.lives -= 1
            if self.lives <= 0:
                self.game_state = "GAMEOVER"

    def update_stars(self, dt: float):
        for star in self.stars:
            star["pos"].y += star["speed"] * dt
            if star["pos"].y > SCREEN_HEIGHT:
                star["pos"].y = 0
                star["pos"].x = random.uniform(0, SCREEN_WIDTH)

    def draw_hud(self):
        score_surf = self.font.render(f"SCORE: {self.score:05d}", True, COLOR_WHITE)
        lives_surf = self.font.render(f"LIVES: {self.lives}", True, COLOR_GREEN)
        self.screen.blit(score_surf, (20, 15))
        self.screen.blit(lives_surf, (SCREEN_WIDTH - 140, 15))
        pygame.draw.line(self.screen, pygame.Color(45, 45, 60), (0, 50), (SCREEN_WIDTH, 50), 2)

    def render_overlay(self, title_text: str, color: pygame.Color):
        title = self.title_font.render(title_text, True, color)
        subtitle = self.font.render("PRESS [ENTER] TO RESTART", True, COLOR_WHITE)
        t_rect = title.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 25))
        s_rect = subtitle.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 35))
        self.screen.blit(title, t_rect)
        self.screen.blit(subtitle, s_rect)

    def run(self):
        while True:
            # pygame-ce: tick() returns milliseconds elapsed; convert to seconds
            dt = self.clock.tick(TARGET_FPS) / 1000.0

            # Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_state == "PLAYING":
                        self.player.shoot(self.player_lasers)
                    if event.key == pygame.K_RETURN and self.game_state != "PLAYING":
                        self.reset_game()

            # Gameplay Logic
            if self.game_state == "PLAYING":
                keys = pygame.key.get_pressed()
                self.player_group.update(dt, keys)
                self.player_lasers.update(dt)
                self.alien_lasers.update(dt)
                self.update_fleet(dt)
                self.handle_alien_fire(dt)
                self.check_collisions()

            self.update_stars(dt)

            # Rendering
            self.screen.fill(COLOR_BLACK)
            for star in self.stars:
                color = COLOR_WHITE if star["radius"] > 1 else pygame.Color(160, 160, 180)
                pygame.draw.circle(self.screen, color, star["pos"], star["radius"])

            self.draw_hud()
            self.player_group.draw(self.screen)
            self.aliens.draw(self.screen)
            self.player_lasers.draw(self.screen)
            self.alien_lasers.draw(self.screen)

            if self.game_state == "GAMEOVER":
                self.render_overlay("GAME OVER", COLOR_RED)
            elif self.game_state == "VICTORY":
                self.render_overlay("SYSTEM SECURED!", COLOR_GREEN)

            pygame.display.flip()

if __name__ == "__main__":
    game = SpaceInvaders()
    game.run()