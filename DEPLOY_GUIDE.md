# HƯỚNG DẪN DEPLOY LÊN GITHUB PAGES

## Bước 1: Tạo tài khoản GitHub (nếu chưa có)
Mở https://github.com/signup → Đăng ký miễn phí

## Bước 2: Tạo Repository mới
1. Đăng nhập vào github.com
2. Nhấn nút **"+"** góc trên phải → **"New repository"**
3. Điền:
   - Repository name: `ept-listening`
   - Chọn **Public** ✅ (bắt buộc để dùng GitHub Pages miễn phí)
   - **KHÔNG** check "Add a README file" (để trống)
4. Nhấn **"Create repository"**

## Bước 3: Copy lệnh push (chạy trong PowerShell)

Sau khi tạo repo, GitHub sẽ hiện trang với lệnh. Chạy các lệnh sau:
(Thay `YOUR_USERNAME` bằng tên tài khoản GitHub của bạn)

```powershell
cd D:\EPT\ept-deploy
git remote add origin https://github.com/YOUR_USERNAME/ept-listening.git
git branch -M main
git push -u origin main
```

## Bước 4: Bật GitHub Pages
1. Vào repo trên GitHub
2. Nhấn tab **"Settings"**
3. Kéo xuống mục **"Pages"** (menu bên trái)
4. Trong "Branch": chọn **main** → **/(root)**
5. Nhấn **Save**
6. Chờ ~2 phút → GitHub Pages sẽ có URL: `https://YOUR_USERNAME.github.io/ept-listening/`

## Lưu ý
- File MP3 dùng Git LFS (hỗ trợ tối đa 1GB miễn phí/tháng)
- Sau khi deploy, truy cập: https://YOUR_USERNAME.github.io/ept-listening/
- Ai cũng có thể vào link này để luyện thi, không cần cùng WiFi!
