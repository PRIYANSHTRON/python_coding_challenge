import pyodbc
from entity.Payment import Payment
from util.DBConnect import DBConnUtil

class PaymentServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()


    def __del__(self):
        """Ensures the database connection is closed when the object is destroyed."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def createPayment(self, payment):
        cursor = self.conn.cursor()
        query = "INSERT INTO Payments (paymentDate, paymentAmount, clientId) VALUES (?, ?, ?)"
        cursor.execute(query, payment.get_paymentDate(), payment.get_paymentAmount(), payment.get_client())
        self.conn.commit()
        return True

    def getPayment(self, paymentId):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Payments WHERE paymentId = ?"
        cursor.execute(query, paymentId)
        result = cursor.fetchone()
        if result:
            return Payment(paymentId=result.paymentId, paymentDate=result.paymentDate, paymentAmount=result.paymentAmount, client=result.clientId)
        else:
            return None

    def getAllPayments(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Payments"
        cursor.execute(query)
        payments = []
        for row in cursor.fetchall():
            payment = Payment(paymentId=row.paymentId, paymentDate=row.paymentDate, paymentAmount=row.paymentAmount, client=row.clientId)
            payments.append(payment)
        return payments

    def updatePayment(self, payment):
        cursor = self.conn.cursor()
        query = "UPDATE Payments SET paymentDate = ?, paymentAmount = ?, clientId = ? WHERE paymentId = ?"
        cursor.execute(query, payment.get_paymentDate(), payment.get_paymentAmount(), payment.get_client(), payment.get_paymentId())
        self.conn.commit()
        return True

    def deletePayment(self, paymentId):
        cursor = self.conn.cursor()
        query = "DELETE FROM Payments WHERE paymentId = ?"
        cursor.execute(query, paymentId)
        self.conn.commit()
        return True