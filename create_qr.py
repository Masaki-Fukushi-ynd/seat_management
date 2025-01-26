import qrcode
import os

# 保存先ディレクトリ
output_dir = "qr_image"

# ディレクトリが存在しなければ作成
os.makedirs(output_dir, exist_ok=True)

# QRコードを0～10まで生成して保存
for i in range(11):  # 0から10まで
    qr = qrcode.QRCode(
        version=1,  # サイズの調整 (1は最小)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # エラー訂正レベル
        box_size=10,  # 1モジュールあたりのサイズ
        border=4,  # QRコードの余白
    )
    qr.add_data(str(i))  # QRコードのデータ
    qr.make(fit=True)

    # QRコードの画像を生成
    img = qr.make_image(fill="black", back_color="white")

    # 画像をファイルに保存
    file_name = f"qr_{i}.png"
    img.save(os.path.join(output_dir, file_name))

print(f"QRコードを {output_dir} フォルダに保存しました。")
