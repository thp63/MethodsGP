class User:
    def _init_(self):
        self.userId =""
        self.loggedIn = False
    def _init_(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
    def login(self):
        pass
    def logout(self):
        pass
    def viewAccountInformation(self):
        pass
    def createAccount(self):
        pass
    def getLoggedIn(self):
        pass
    def setUserId(self, value):
        self.setUserId = value
    def getUserId(self):
        return self.userId
    def setdbName(self, value):
        self.dbName = value
    def getdbName(self):
        return self.dbName
    def setTableName(self, value):
        self.tableName = value
    def getTableName(self):
        return self.tableName
    