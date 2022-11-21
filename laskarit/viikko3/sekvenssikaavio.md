sequenceDiagram
		Machine ->> tank: FuelTank()
		Machine ->> FuelTank: fill(40)
		activate FuelTank
		FuelTank ->> tank: fuel_contents(40)
		FuelTank --> Machine
		deactivate FuelTank
		Machine ->> engine: Engine(tank)
		Machine ->> Engine: start()
		activate Engine
		Engine ->> tank: consume(5)
		
		
