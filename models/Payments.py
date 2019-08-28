from config.config import db


class C2bPayment(db.Model):
    __tablename__ = 'mpesa_payments'
    id = db.Column(db.Integer, primary_key=True)
    TransactionType = db.Column(db.String())
    TransID = db.Column(db.String())
    TransTime = db.Column(db.String())
    TransAmount = db.Column(db.Float())
    BusinessShortCode = db.Column(db.String())
    BillRefNumber = db.Column(db.String())
    InvoiceNumber = db.Column(db.String())
    ThirdPartyTransID = db.Column(db.String())
    MSISDN = db.Column(db.String())
    FirstName = db.Column(db.String())
    MiddleName = db.Column(db.String())
    LastName = db.Column(db.String())
    OrgAccountBalance = db.Column(db.String())

    # insert records
    def insert_transactions(self):
        db.session.add(self)
        db.session.commit()
        return self

    # fetch all transactions
    @classmethod
    def fetch_all(cls):
        return cls.query.all()
