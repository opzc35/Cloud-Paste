import firebase_admin
from firebase_admin import credentials, db
import pyperclip  # 用于获取剪贴板内容

# 初始化 Firebase Admin SDK
cred = credentials.Certificate('path_to_your_firebase_adminsdk.json')  # 替换为下载的 JSON 文件路径
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-name.firebaseio.com'  # 替换为你的 Firebase Realtime Database URL
})

# 获取 Firebase Realtime Database 的引用
ref = db.reference('clipboard')

def upload_clipboard_data():
    clipboard_data = pyperclip.paste()  # 获取当前剪贴板的文本内容
    if clipboard_data:
        ref.set(clipboard_data)  # 上传到 Firebase Realtime Database
        print("上传剪贴板数据成功!")
    else:
        print("剪贴板为空!")

# 调用函数上传剪贴板内容
upload_clipboard_data()
