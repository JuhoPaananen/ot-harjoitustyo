```mermaid
classDiagram
	Peli "1" -- "1" Pelilauta
	Peli "1" -- "2" Noppa
	Peli "1" -- "2..8" Pelaaja
	Ruutu "40" -- "1" Pelilauta
	Pelaaja "1" -- "1" Pelinappula
	Ruutu "1" -- "1..8" Pelinappula

```
