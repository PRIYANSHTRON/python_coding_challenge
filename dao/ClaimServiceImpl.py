import pyodbc
from entity.Claim import Claim
from util.DBConnect import DBConnUtil

class ClaimServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def __del__(self):
        """Ensures the database connection is closed when the object is destroyed."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def createClaim(self, claim):
        cursor = self.conn.cursor()
        query = "INSERT INTO Claims (claimNumber, dateFiled, claimAmount, status, clientId, policy) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, claim.get_claimNumber(), claim.get_dateFiled(), claim.get_claimAmount(), claim.get_status(), claim.get_client(), claim.get_policy())
        self.conn.commit()
        return True

    def getClaim(self, claimId):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Claims WHERE claimId = ?"
        cursor.execute(query, claimId)
        result = cursor.fetchone()
        if result:
            return Claim(claimId=result.claimId, claimNumber=result.claimNumber, dateFiled=result.dateFiled, claimAmount=result.claimAmount, status=result.status, clientId=result.clientId, policy=result.policy)
        else:
            return None

    def getAllClaims(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Claims"
        cursor.execute(query)
        claims = []
        for row in cursor.fetchall():
            claim = Claim(claimId=row.claimId, claimNumber=row.claimNumber, dateFiled=row.dateFiled, claimAmount=row.claimAmount, status=row.status, clientId=row.clientId, policy=row.policy)
            claims.append(claim)
        return claims

    def updateClaim(self, claim):
        cursor = self.conn.cursor()
        query = "UPDATE Claims SET claimNumber = ?, dateFiled = ?, claimAmount = ?, status = ?, clientId = ?, policy = ? WHERE claimId = ?"
        cursor.execute(query, claim.get_claimNumber(), claim.get_dateFiled(), claim.get_claimAmount(), claim.get_status(), claim.get_clientId(), claim.get_policy(), claim.get_claimId())
        self.conn.commit()
        return True

    def deleteClaim(self, claimId):
        cursor = self.conn.cursor()
        query = "DELETE FROM Claims WHERE claimId = ?"
        cursor.execute(query, claimId)
        self.conn.commit()
        return True