# Arkkitehtuurikuvaus
## Rakenne
Ohessa kuvattu rakenne luokkakaaviona

```mermaid
classDiagram
AsteroidsGame "1" -- "*" Asteroid
AsteroidsGame "1" -- "1" Player
AsteroidsGame "1" -- "0...5" Bullet
Asteroid <|-- FlyingObject
Player  <|-- FlyingObject
Bullet <|-- FlyingObject

class FlyingObject {
Vector2 heading
Vector2 speed
move()
draw()
}
```

## Päätoiminnallisuudet 
Ohessa pelin keskeiset toiminallisuudet kuvattuna sekvenssikaaviona
### Ampuminen

```mermaid
sequenceDiagram
main->>game: AsteroidsGame():
game ->> game: shoot()
game ->> objects: Bullet(Player.position, bullet_speed)
```
Onkohan pelin rakenne jotenkin todella vaikea, jos on vaikeuksia luoda mielekästä sekvenssikaaviota toiminnallisuuksista?
