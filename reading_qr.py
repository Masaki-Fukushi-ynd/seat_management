import cv2
import requests
import time

# サーバーのエンドポイントURL
url = "http://localhost:3000/seats/update"

# APIキーを設定
api_key = 'c9b3d1e8a97b0fd340ed9db4e75d6d74a6bb6a1f7f0e1c2e0ff35d547774276d'
headers = {'X-API-KEY': api_key} # リクエストヘッダーにAPIキーを追加

detected_qrs = set()  # QRコードのデータを格納するセット

# QRCodeDetector を初期化
qr_detector = cv2.QRCodeDetector()

# カメラを起動
cap = cv2.VideoCapture(0)

print("QRコードをカメラでスキャンしてください。'q'キーで終了します。")

start_time = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        print("カメラから映像を取得できませんでした。")
        break

    # QRコードを検出してデコード
    data, bbox, _ = qr_detector.detectAndDecode(frame)

    if data:    
        detected_qrs.add(int(data))  # 重複を避けデータをセットに追

        
    if time.time() - start_time >= 5:
        try:
            response = requests.post(url, json={"data": list(detected_qrs)}, headers=headers)
            response.raise_for_status()  # HTTPエラーの場合例外を発生させる
        except requests.exceptions.HTTPError as e:
            print(f"HTTPエラー: {e}")
        except requests.exceptions.RequestException as e:
            print(f"サーバーへの通信エラー: {e}")

        start_time = time.time()
        detected_qrs.clear()

    # 映像を画面に表示
    cv2.imshow("QRコードリーダー", frame)

    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
