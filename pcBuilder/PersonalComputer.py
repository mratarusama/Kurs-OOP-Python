from detailEnum import *
import dbInterface
import Details
import dynMenu

class buildPC(object):
    def __init__(self):
        self.db = dbInterface.createDB('details.db')
        self.Body = None
        self.Motherboard = None
        self.CPU = None
        self.Cooler = None
        self.GPU = None
        self.RAM = None
        self.Drives = None
        self.PowSupply = None
        self.createMenu()

    def createMenu(self):
        self.pc = dynMenu.Menu("Your Personal Computer")
        self.pc.register_action(self.getMyPrefs, "Get my current set")
        self.pc.register_action(self.changeBody, "Change PC case")
        self.pc.register_action(self.changeMother, "Change motherboard")
        self.pc.register_action(self.changeCPU, "Change CPU")
        self.pc.register_action(self.changeCooler, "Change Cooler")
        self.pc.register_action(self.changeGPU, "Change graphic card")
        self.pc.register_action(self.changeRAM, "Change RAM")
        self.pc.register_action(self.changeDrives, "Change drives")
        self.pc.register_action(self.changePowerSupply, "Change power supply")
        self.pc.register_action(self.tryToRun, "Try to run PC")
        self.pc.start()

    def getMyPrefs(self):
        totalCost = 0
        print('My current set:')
        if self.Body:
            totalCost += self.Body.cost
            print('\tCase:', self.Body.name)
            print('\t\tFormat:', self.Body.mFormat.name)
            print('\t\tMax videocard:', self.Body.maxVideo)
            print('\t\tMax cooler:', self.Body.maxCooler)
        else:
            print('\tCase: None')
            
        if self.Motherboard:
            totalCost += self.Motherboard.cost
            print('\n\tMotherboard:', self.Motherboard.name)
            print('\t\tSocket:', self.Motherboard.socket)
            print('\t\tRAM:', self.Motherboard.ramSupport.name)
            print('\t\tFormat:', self.Motherboard.mFormat.name)
        else:
            print('\n\tMotherboard: None')
        if self.CPU:
            totalCost += self.CPU.cost
            print('\n\tCPU:', self.CPU.name)
            print('\t\tSocket:', self.CPU.socket)
            print('\t\tFrequency:', self.CPU.freq)
            print('\t\tTDP:', self.CPU.tdp)
            print('\t\tIntegrated graphic:', 'Yes' if self.CPU.graphics else 'No')
        else:
            print('\n\tCPU: None')
        
        if self.Cooler:
            totalCost += self.Cooler.cost
            print('\b\tCooler:', self.Cooler.name)
            print('\t\tTDP:', self.Cooler.tdp)
            print('\t\tHeight:', self.Cooler.height)
        else:
            print('\n\tCooler: None')
        
        if self.GPU:
            totalCost += self.GPU.cost
            print('\n\tGPU:', self.GPU.name)
            print('\t\tVideo volume:', self.GPU.vRAM)
            print('\t\tMax power usage:', self.GPU.maxPowConsumption)
            print('\t\tLength:', self.GPU.length)
        else:
            print('\n\tGPU: None')
            
        if self.RAM:
            totalCost += self.RAM.cost
            print('\n\tRAM:', self.RAM.name)
            print('\t\tMemory type:', self.RAM.memType.name)
            print('\t\tVolume:', self.RAM.volume)
            print('\t\tFrequency:', self.RAM.freq)
            print('\t\tMax power', self.RAM.power)
        else:
            print('\n\tRAM: None')
            
        if self.Drives:
            totalCost += self.Drives.cost
            print('\n\tDrives:', self.Drives.name)
            print('\t\tVolume:', self.Drives.volume)
            if isinstance(self.Drives, Details.HDD):
                print('\t\tSpindle speed:', self.Drives.spinSpeed)
                print('\t\tMax pow:', self.Drives.maxPower)
            else:
                print('\t\tMax write speed:', self.Drives.maxIn)
                print('\t\tMax read speed:', self.Drives.maxOut)
        else:
            print('\n\tDrives: None')
            
        if self.PowSupply:
            totalCost += self.PowSupply.cost
            print('\n\tPower supply:', self.PowSupply.name)
            print('\t\tMax power:', self.PowSupply.maxPower)
            print('\t\tEnergy efficienct cert:', self.PowSupply.eEfficiency.name)
        else:
            print('\n\tPower supply: None')
            
        print('\nTotal cost:', totalCost)
        input('\nPress Enter to leave this screen')

    def buildChangeMenu(self, unit):
        det = self.db.getTableRows(unit)
        titLine = ''
        for l in det:
            titLine += l[0] + '; '
        newMenu = dynMenu.Menu(titLine, True, self.pc)
        det = self.db.getAllDetails(unit)
        for c in det:
            line = ''
            for l in c:
                line += str(l) + '; '
            newMenu.register_action(None, line)
        newMenu.start()
        if newMenu.selected == 1:
            return None
        else:
            return det[newMenu.selected - 2]

    def changeBody(self):
        newDetail = self.buildChangeMenu('pCase')
        if newDetail:
            if self.Body:
                del self.Body
            self.Body = Details.Body(newDetail[0], newDetail[1], MotherFormats[newDetail[2]], newDetail[3], newDetail[4])
        return 0
    
    def changeMother(self):
        newDetail = self.buildChangeMenu('Motherboard')
        if newDetail:
            if self.Motherboard:
                del self.Motherboard
            self.Motherboard = Details.Motherboard(newDetail[0], newDetail[1], newDetail[2], MemType[newDetail[3]], MotherFormats[newDetail[4]])
        return 0
    
    def changeCPU(self):
        newDetail = self.buildChangeMenu('CPU')
        if newDetail:
            if self.CPU:
                del self.CPU
            self.CPU = Details.Porcessor(newDetail[0], newDetail[1], newDetail[2], newDetail[3], newDetail[4], newDetail[5])
        return 0
    
    def changeCooler(self):
        newDetail = self.buildChangeMenu('Cooler')
        if newDetail:
            if self.Cooler:
                del self.Cooler
            self.Cooler = Details.Cooler(newDetail[0], newDetail[1], newDetail[2], newDetail[3])
        return 0    
    
    def changeGPU(self):
        newDetail = self.buildChangeMenu('Videocard')
        if newDetail:
            if self.GPU:
                del self.GPU
            self.GPU = Details.Videocard(newDetail[0], newDetail[1], newDetail[2], newDetail[3], newDetail[4])
        return 0
    
    def changeRAM(self):
        newDetail = self.buildChangeMenu('RAM')
        if newDetail:
            if self.RAM:
                del self.RAM
            self.RAM = Details.RAM(newDetail[0], newDetail[1], MemType[newDetail[2]], newDetail[3], newDetail[4], newDetail[5])
        return 0
    
    def changeDrives(self):
        q = dynMenu.Menu('What do you want to install?', True, self.pc)
        q.register_action(None, 'HDD')
        q.register_action(None, 'SSD')
        q.start()
        if q.selected > 1:
            newDetail = self.buildChangeMenu(q.result)
            if newDetail:
                if self.Drives:
                    del self.Drives
                
                if q.selected == 2:
                    self.Drives = Details.HDD(newDetail[0], newDetail[1], newDetail[2], newDetail[3], newDetail[4])       
                else:
                    self.Drives = Details.SSD(newDetail[0], newDetail[1], newDetail[2], newDetail[3], newDetail[4])       
        return 0
    
    def changePowerSupply(self):
        newDetail = self.buildChangeMenu('powSuply')
        if newDetail:
            if self.PowSupply:
                del self.PowSupply
            self.PowSupply = Details.PowSuply(newDetail[0], newDetail[1], newDetail[2], energyCert[newDetail[3]])        
        
    
    def tryToRun(self):
        if not self.Body:
            input('I don\'t see your case')
            return -1
        if not self.Motherboard:
            input('I don\'t see your motherboard')
            return -1
        if not self.CPU:
            input('I don\'t see your CPU')
            return -1
        if not self.Cooler:
            input('I don\'t see your Cooler')
            return -1
        if not self.GPU and not self.CPU.graphics:
            input('I don\'t see your video card')
            return -1
        if not self.RAM:
            input('I don\'t see your RAM')
            return -1
        if not self.Drives:
            input('I don\'t see your Drives')
            return -1
        if not self.PowSupply:
            input('I don\'t see your Power supply')
        
        if self.Body.mFormat.value < self.Motherboard.mFormat.value:
            print('Oh No, I think you broke your motherboard trying to fit it into the wrong case ;c')
            input(self.Motherboard.name + ', rest in peace')
            del self.Motherboard
            self.Motherboard = None
            return -1
        if self.Motherboard.socket != self.CPU.socket:
            print('Oh No, I think you broke your CPU trying to fit it into wrong motherboard socket ;c')
            input(self.CPU.name + ', rest in peace')
            del self.CPU
            self.CPU = None
            return -1
        if self.Motherboard.ramSupport.value != self.RAM.memType.value:
            print('Oh No, I think you broke your RAM trying to fit it into wrong motherboard socket ;c')
            input(self.RAM.name + ', rest in peace')
            del self.RAM
            self.RAM = None
            return -1
        if self.GPU:
            if self.Body.maxVideo < self.GPU.length:
                print('Oh No, I think you broke your Сase trying to fit a longer video card into it ;c')
                input(self.Body.name + ', rest in peace')
                del self.GPU
                self.GPU = None
                return -1
        if self.Body.maxCooler < self.Cooler.height:
            print('Oh No, I think you broke your Сase trying to fit a taller cooler into it ;c')
            input(self.Body.name + ', rest in peace')
            del self.GPU
            return -1
        
        totalPower = 11
        totalPower += self.CPU.tdp
        if self.GPU:
            totalPower += self.GPU.maxPowConsumption
        totalPower += self.RAM.power
        if isinstance(self.Drives, Details.HDD):
            totalPower += self.Drives.maxPower
        
        if (self.PowSupply.maxPower * self.PowSupply.eEfficiency.value) < totalPower:
            print('Oh No, I think you burned your Power supply ;c')
            input(self.PowSupply.name + ', rest in peace')
            del self.PowSupply
            return -1            
        
        print('Congratulations, your build is working c;\n\n')
        print('                               .,,uod8B8bou,,.')
        print('              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.')
        print('         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||')
        print('         !...:!TVBBBRPFT||||||||||!!^^""\'   ||||')
        print('         !.......:!?|||||!!^^""\'            ||||')
        print('         !.........||||                     ||||')
        print('         !.........||||  ##                 ||||')
        print('         !.........||||                     ||||')
        print('         !.........||||                     ||||')
        print('         !.........||||                     ||||')
        print('         !.........||||                     ||||')
        print('         `.........||||                    ,||||')
        print('          .;.......||||               _.-!!|||||')
        print('   .,uodWBBBBb.....||||       _.-!!|||||||||!:\'')
        print('!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....')
        print('!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.')
        print('!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.')
        print('!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.')
        print('!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.')
        print('`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.')
        print('  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^\'')
        print('    `........::::::::::::::::;iof688888888888888888888b.     `')
        print('      `......:::::::::;iof688888888888888888888888888888b.')
        print('        `....:::;iof688888888888888888888888888888888899fT!')
        print('          `..::!8888888888888888888888888888888899fT|!^"\'')
        print('            `\' !!988888888888888888888888899fT|!^"\'')
        print('                `!!8888888888888888899fT|!^"\'')
        print('                  `!988888888899fT|!^"\'')
        print('                    `!9899fT|!^"\'')
        print('                      `!^"\'')
        input()
        return 0