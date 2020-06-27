-- Processor
create table CPU (
	Costs integer not null,				-- Cost of the part in rubles, exmpl "1799", "4299" etc.
	Name varchar(64) not null,			-- Part name, exmpl "AeroCool Verkho A-3P", "AMD Athlon 3000G OEM" etc.
	Socket varchar(10) not null,		-- Socket, exmpl "LGA1200", "FM2+" etc.
	Frequency integer not null,			-- Frequency, exmpl "1450", "3000" etc.
	TDP integer not null,				-- Heat dissipation, exmpl "165", "110"
	Graphic boolean not null			-- Is there an integrated video card (Yes/No)
);

-- CPU Cooler
create table Cooler (
	Costs integer not null,				-- Cost of the part in rubles, exmpl "1799", "4299" etc.
	Name varchar(64) not null,			-- Part name, exmpl "AeroCool Verkho A-3P", "AMD Athlon 3000G OEM" etc.
	TDP integer not null,				-- Dissipated power, exmpl "165", "110"
	Height integer not null				-- Height of the cooler, exmpl "43", "55" etc.
);

-- Motherboard
create table Motherboard (
	Costs integer not null,				-- Cost of the part in rubles, exmpl "1799", "4299" etc.
	Name varchar(64) not null,			-- Part name, exmpl "AeroCool Verkho A-3P", "AMD Athlon 3000G OEM" etc.
	Socket varchar(10) not null,		-- CPU Socket, exmpl "LGA1200", "FM2+" etc.
	RAMSupport varchar(10) not null,	-- Supported RAM type, exmpl "DDR2", "DDR3L" etc.
	mFormat varchar(10) not null		-- Motherboard format, exmpl "microATX", "ATX" etc.
);

-- Videocard
create table Videocard (
	Costs integer not null,				-- Cost of the part in rubles, exmpl "1799", "4299" etc.
	Name varchar(64) not null,			-- Part name, exmpl "AeroCool Verkho A-3P", "AMD Athlon 3000G OEM" etc.
	vRAM integer not null,				-- Video memory volume, exmpl "2", "4" etc.
	maxPow integer not null,			-- Max power consumption, exmpl "165", "215" etc.
	cardLength integer not null			-- Videocard length, exmpl "297", "155" etc.
);

-- RAM
create table RAM (
	Costs integer not null,				-- Cost of the part in rubles, exmpl "1799", "4299" etc.
	Name varchar(64) not null,			-- Part name, exmpl "AeroCool Verkho A-3P", "AMD Athlon 3000G OEM" etc.
	memType varchar(10) not null,		-- RAM type, exmpl "DDR2", "DDR3L" etc.
	Volume integer not null,			-- RAM Volume, exmpl "8", "16" etc.
	Frequency integer not null,			-- RAM Frequency, exmpl "1600", "1333" etc.
	mPower double not null				-- Supply voltage, exmpl "1.5", "0.4" etc.
);

-- Body
create table pCase (
	Costs integer not null,				-- Cost of the part in rubles, exmpl "1799", "4299" etc.
	Name varchar(64) not null,			-- Part name, exmpl "AeroCool Verkho A-3P", "AMD Athlon 3000G OEM" etc.
	mFormat varchar(10) not null,		-- Motherboard format, exmpl "microATX", "ATX" etc.
	maxVideo integer not null,			-- Max length of videocard, exmpl "297", "155" etc.
	maxCooler integer not null			-- Max cooler height, exmpl "43", "55" etc.
);

-- HDD
create table HDD (
	Costs integer not null,				-- Cost of the part in rubles, exmpl "1799", "4299" etc.
	Name varchar(64) not null,			-- Part name, exmpl "AeroCool Verkho A-3P", "AMD Athlon 3000G OEM" etc.
	Volume integer not null,			-- Data capacity, exmpl "5000", "1000" etc.
	spinSpeed integer not null,			-- Spindle speed, exmpl "5700", "7200" etc. 
	maxPower double not null			-- Maximum power consumption, exmpl "6.4", "3.7" etc.
);

-- SSD
create table SSD (
	Costs integer not null,				-- Cost of the part in rubles, exmpl "1799", "4299" etc.
	Name varchar(64) not null,			-- Part name, exmpl "AeroCool Verkho A-3P", "AMD Athlon 3000G OEM" etc.
	Volume integer not null,			-- Data capacity, exmpl "5000", "1000" etc.
	maxIn integer not null,				-- Max write speed, exmpl "440", "490" etc.
	maxOut integer not null				-- Max read speed, exmpl "125", "360" etc.
);

-- Power Supply
create table powSuply(
	Costs integer not null,				-- Cost of the part in rubles, exmpl "1799", "4299" etc.
	Name varchar(64) not null,			-- Part name, exmpl "AeroCool Verkho A-3P", "AMD Athlon 3000G OEM" etc.
	maxPower integer not null,			-- Maximum power capacity
	eEfficiency varchar(10) not null		-- Energy efficiency certificate 80+, exmpl "Standart", "Platinum" etc.
);