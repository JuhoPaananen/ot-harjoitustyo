```mermaid
sequenceDiagram
		main->>laitehallinto: HKLLaitehallinto()
		main->>rautatietori: Lataajalaite()
    main->>ratikka6: Lukijalaite()
    main->>bussi244: Lukijalaite()
		main->>laitehallinto: lisaa_lataaja(rautatietori)
		main->>laitehallinto: lisaa_lukija(ratikka6)
		main->>laitehallinto: lisaa_lukija(bussi244)
		main->>lippu_luukku: Kioski()
		main->>lippu_luukku: osta_matkakortti("Kalle)
		activate lippu_luukku
		lippu_luukku->>kallen_kortti: Matkakortti("Kalle")
		kallen_kortti-->>lippu_luukku: 
		deactivate lippu_luukku
		lippu_luukku-->>main: 
		main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
		activate rautatietori
		rautatietori->>kallen_kortti: kasvata_arvoa(3)
		kallen_kortti-->>rautatietori: 
		rautatietori-->> main: 
		deactivate rautatietori
		main->>ratikka6: osta_lippu(kallen_kortti, 0)
		activate ratikka6
		ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
		
```