-- 10 elements of each type will be selected for demonstration


-- Processor
insert into CPU values
	(3499, 'AMD Athlon 3000G OEM', 'AM4', 3500, 65, True),
	(3999, 'Intel Pentium Gold G5600F OEM', 'LGA 1151-v2', 3900, 51, False),
	(9099, 'AMD Ryzen 5 2600X OEM', 'AM4', 3600, 95, False),
	(10699, 'Intel Core i3-8300 OEM', 'LGA 1151-v2', 3700, 62, True),
	(11399, 'AMD Ryzen 5 3400G OEM', 'AM4', 3700, 65, True),
	(11799, 'Intel Core i5-9400F OEM', 'LGA 1151-v2', 2900, 65, False),
	(12199, 'AMD Ryzen 5 3600 OEM', 'AM4', 3600, 65, False),
	(12299, 'Intel Core i5-9400F OEM', 'LGA 1151-v2', 2900, 65, False),
	(16199, 'Intel Core i5-10400 OEM', 'LGA 1200', 2900, 65, True),
	(21499, 'AMD Ryzen 7 3700X OEM', 'AM4', 3600, 65, False);


-- CPU Cooler
insert into Cooler values
	(370, 'ID-Cooling DK-01S', 65, 43),
	(499, 'PCCooler E90 [CLPCC_E90]', 75, 57),
	(720, 'Сooler Master i50 [RH-I50-20PK-R1]', 65, 80),
	(930, 'Arctic Cooling Alpine 64 PLUS [UCACO-AP60301-BUA01]', 90, 70),
	(999, 'CoolerMaster X Dream i117 RR-X117-18FP-R1', 70, 61),
	(1250, 'ID-Cooling IS-25i', 75, 27),
	(1499, 'Akasa K32 [AK-CC7117EP01]', 95, 63),
	(1999, 'DEEPCOOL GAMMAXX 400 (WHITE BASIC) [DP-MCH4-GMX400P-WH]', 130, 155),
	(2450, 'PCCooler GI-46U CORONA B [GI-46U CORONA B]', 125, 75),
	(3499, 'Xilence Perfomance A+ M704 ARGB [XC055]', 180, 160);


-- Motherboard
insert into Motherboard values
	(3299, 'GIGABYTE GA-A320M-H', 'AM4', 'DDR4', 'microATX'),
	(3450, 'ASRock H310CM-HDV', 'LGA 1151-v2', 'DDR4', 'microATX'),
	(3750, 'ASUS PRIME A320M-K', 'AM4', 'DDR4', 'microATX'),
	(3950, 'GIGABYTE H310M S2H 2.0', 'LGA 1151-v2', 'DDR4', 'microATX'),
	(4599, 'MSI A320M-A PRO-M2', 'AM4', 'DDR4', 'microATX'),
	(4650, 'ASUS PRIME B360M-K', 'LGA 1151-v2', 'DDR4', 'microATX'),
	(4699, 'MSI B450M-A PRO MAX', 'AM4', 'DDR4', 'microATX'),
	(4999, 'GIGABYTE GA-H310TN', 'LGA 1151-v2', 'DDR4', 'miniITX'),
	(6499, 'Biostar X470GTA Ver.5.x', 'AM4', 'DDR4', 'ATX'),
	(6599, 'ASUS PRIME H310-PLUS R2.0', 'LGA 1151-v2', 'DDR4', 'ATX');


-- Videocard
insert into Videocard values
	(4599, 'Palit GeForce GT 730 [NE5T7300HD46-2087F]', 2, 25, 160),
	(5499, 'PowerColor AMD Radeon RX 550 Red Dragon [AXRX 550 2GBD5-DHA/OC]', 2, 50, 210),
	(5699, 'MSI GeForce GT 1030 AERO ITX OC [GT 1030 AERO ITX 2GD4 OC]', 2, 20, 147),
	(6499, 'Sapphire AMD Radeon RX 550 PULSE OC [11268-01-20G]', 4, 65, 128),
	(10499, 'ASUS GeForce GTX 1050 PHOENIX [PH-GTX1050-2G]', 2, 75, 192),
	(10699, 'ASUS AMD Radeon RX 560 STRIX [STRIX-RX560-4G-GAMING]', 4, 80, 194),
	(12299, 'GTX 1650 DUAL OC [DUAL-GTX1650-O4G]', 4, 75, 204),
	(12399, 'Sapphire AMD Radeon RX 570 PULSE [11266-66-20G]', 8, 180, 230),
	(16499, 'KFA2 GeForce GTX 1660 [60SRH7DSY91K]', 6, 120, 228),
	(16499, 'MSI AMD Radeon RX 5500 XT MECH OC [RX 5500 XT MECH 8G OC]', 8, 140, 215);

-- RAM
insert into RAM values
	(980, 'Kingston ValueRAM [KVR13N9S6/2]', 'DDR3', 2, 1333, 1.5),
	(1299, 'Kingston ValueRAM [KVR26N19S6/4]', 'DDR4', 4, 2666, 1.2),
	(1599, 'Patriot Viper Elite [PVE44G240C6GY]', 'DDR4', 4, 2400, 1.2),
	(2499, 'Kingston ValueRAM [KVR24N17S8/8]', 'DDR4', 8, 2400, 1.2),
	(3099, 'Patriot Signature Line Premium [PSP48G2400KH1]', 'DDR4', 8, 2400, 2.4),
	(3399, 'HP V6 [7EH67AA]', 'DDR4', 8, 3200, 1.35),
	(3499, 'Crucial Ballistix Black [BL2K4G24C16U4B]', 'DDR4', 4, 2400, 1.35),
	(4299, 'Kingston HyperX Predator RGB [HX432C16PB3A/8]', 'DDR4', 8, 3200, 1.35),
	(4899, 'Apacer [EL.16G2T.GFH]', 'DDR4', 16, 2400, 1.2),
	(5499, 'Goodram Iridium [IR-XR2666D464L16S/16GDC]', 'DDR4', 16, 2666, 2.7);


-- Body
insert into pCase values
	(1199, 'DEXP DC-201M', 'microATX', 300, 142),
	(2050, 'ZALMAN T6', 'microATX', 280, 165),
	(2699, 'Aerocool AERO-300', 'ATX', 372, 160),
	(2999, 'CoolerMaster Elite 342 [RC-342-KKN6-U3]', 'microATX', 363, 153),
	(2999, 'Thermaltake Versa H22', 'ATX', 315, 155),
	(3199, 'Aerocool Rift BG', 'ATX', 371, 155),
	(3750, 'Deepcool MATREXX 55 [DP-ATX-MATREXX55]', 'ATX', 370, 168),
	(4050, 'Deepcool MATREXX 55 V3 ADD-RGB [DP-ATX-MATREXX55V3-AR]', 'EATX', 370, 168),
	(4999, 'CoolerMaster MasterBox MB520 [MCB-B520-KANN-S00]', 'ATX', 410, 165),
	(5699, 'SilverStone Milo ML-06 [SST-ML06B]', 'miniITX', 193, 70);


-- HDD
insert into HDD values
	(2550, 'Toshiba P300 [HDWD105UZSVA]', 500, 7200, 6.4),
	(4299, 'Seagate 5900 IronWolf [ST1000VN002]', 1000, 5900, 3.6),
	(5050, 'Seagate 5900 SkyHawk [ST2000VX008]', 2000, 5900, 5.6),
	(6999, 'Seagate 7200 FireCuda [ST2000DX002]', 2000, 7200, 6.7),
	(7899, 'Toshiba X300 [HDWE140UZSVA]', 4000, 7200, 11.3),
	(9799, 'Toshiba [MG04ACA400E]', 4000, 7200, 11.3),
	(11799, 'Toshiba Enterprise Capacity [MG06ACA600E]', 6000, 7200, 8.3),
	(12999, 'Seagate 7200 Exos 7E8 [ST6000NM0115]', 6000, 7200, 12.11),
	(14299, 'Seagate BarraCuda [ST8000DM004]', 8000, 5400, 5.3),
	(15099, 'Toshiba Enterprise Capacity [MG06ACA800E]', 8000, 7200, 9.1);


--SSD
insert into SSD values
	(1500, 'Apacer AS350 PANTHER [AP120GAS350-1]', 120, 440, 125),
	(1999, 'Smartbuy Jolt [SB120GB-JLT-25SAT3]', 120, 500, 450),
	(2250, 'Pioneer APS-SL3N [APS-SL3N-128]', 128, 550, 450),
	(2799, 'SiliconPower Ace A58 [SP256GBSS3A58A25]', 256, 510, 480),
	(2999, 'Smartbuy Splash [SBSSD-256GT-MX902-25S3]', 256, 560, 500),
	(4550, 'DEXP XL2 [SSB512GMLCMSB2CD-DR0E]', 512, 500, 480),
	(4899, 'SiliconPower Ace A58 [SP512GBSS3A58A25]', 512, 510, 480),
	(5299, 'SiliconPower Ace A56 [SP512GBSS3A56B25RM]', 512, 560, 530),
	(8499, 'Goodram CX400 [SSDPR-CX400-01T]', 1024, 550, 490),
	(11899, 'Hikvision E100 [HS-SSD-E100/1024G]', 1024, 560, 500);


-- Power Supply
insert into PowSuply values
	(1850, 'Xilence Gaming series XN213 450W [XP450R10]', 450, 'Bronze'),
	(2899, 'Chieftec TFX 300W [GPF-300P]', 300, 'Bronze'),
	(2899, 'Deepcool DN 500W [DN500]', 500, 'Standart'),
	(3199, 'be quiet! SFX POWER 2 300W [BN226]', 300, 'Bronze'),
	(3650, 'CoolerMaster MWE 550 WHITE - V2 [MPE-5501-ACABW-EU]', 550, 'Standart'),
	(3999, 'Aerocool KCAS RGB 750W [KCAS-750G]', 750, 'Gold'),
	(4550, 'Chieftec 650W [GDP-650C]', 650, 'Gold'),
	(5399, 'Seasonic SSP-350GT [SSP-350GT Active PFC F3]', 350, 'Gold'),
	(10199, 'Fractal Design Ion+ 560P [FD-PSU-IONP-560P-BK]', 560, 'Platinum'),
	(18999, 'Seasonic Prime ULTRA 750W [SSR-750TR]', 750, 'Titanium');