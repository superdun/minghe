from flask import Flask


SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost:3306/minghe'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '123456'

QINIU_ACCESS_KEY = 'u1M-QQ-m0ciNAhDn2AZ6iODyKnjUmY7EW1uH2ZiZ'
QINIU_SECRET_KEY = 'QN3dDZvbX5MdDxfWsf4vua774Wz_5JFCZP78PGTU'
QINIU_BUCKET_NAME = 'makerimg'
QINIU_BUCKET_DOMAIN = 'oc1is8h9w.bkt.clouddn.com'


FACE_KEY = "ZfZkvZVgtmq023KgiYjj8zYp-eGmG-wJ"
FACE_API_KEY = "F2pl2jjyeTtSFPIllQ-MCF9HT2DPqRv5"
#REDIS_URL = "redis://superdun:1786e7e78a4cc86cba72c38edf4fc33f@50.30.35.9:3616/"
REDIS_URL ='redis://@127.0.0.1:6379/'
