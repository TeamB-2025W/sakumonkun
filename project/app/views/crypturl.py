from django.core import signing

def generate_exam_url(testid):
    signed_testid = signing.dumps({"testid": testid})  # 署名付きデータを生成
    return signed_testid

def verify_exam_url(signed_testid):
    try:
        data = signing.loads(signed_testid)  # 署名を検証 & 復号
        return data["testid"]
    except signing.BadSignature:
        return None  # 署名が無効ならエラー
    

def generate_exam_result_url(examinationid):
    signed_examinationid = signing.dumps({"examinationid": examinationid})  # 署名付きデータを生成
    return signed_examinationid

def verify_exam_result_url(signed_examinationid):
    try:
        data = signing.loads(signed_examinationid)  # 署名を検証 & 復号
        return data["examinationid"]
    except signing.BadSignature:
        return None  # 署名が無効ならエラー