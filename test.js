<script>
  async function checkLogin() {
    const user = document.getElementById('login-user').value;
    const pass = document.getElementById('login-pass').value;
    
    try {
      /* const res = await fetch('/api/login', {
        method: 'POST',
        body: JSON.stringify({user, pass})
      }); */
      if(!user.trim()) { showLoginError('Vui lòng nhập MSSV (Mã số sinh viên)'); return; }
        const data = {success: true};
      
      if (data.success) {
        window.currentUser = user;
        
        // Sync history
        
        const state = {};
        if (Object.keys(state).length > 0) {
            localStorage.setItem(SK, JSON.stringify(state));
        }
        
        document.getElementById('login-overlay').classList.add('hidden');
        document.body.classList.remove('locked');
        localStorage.setItem('ept_auth', user);
        
        // Show module select instead of home
        $('module-select').style.display = 'block';
      } else {
        showLoginError(data.error || "Đăng nhập thất bại");
      }
    } catch (e) {
      showLoginError("Lỗi kết nối máy chủ!");
    }
  }
  
  function showLoginError(msg) {
      const err = document.getElementById('login-error');
      err.textContent = msg;
      err.style.display = 'block';
      err.animate([{transform: 'translateX(-5px)'}, {transform: 'translateX(5px)'}, {transform: 'translateX(0)'}], {duration: 300});
  }

  document.addEventListener('DOMContentLoaded', async () => {
    const savedUser = localStorage.getItem('ept_auth');
    if (savedUser) {
      window.currentUser = savedUser;
      document.getElementById('login-overlay').style.display = 'none';
      document.body.classList.remove('locked');
      
      try {
        const state = {};
        if (Object.keys(state).length > 0) {
            localStorage.setItem(SK, JSON.stringify(state));
        }
        $('home').style.display = 'block';
        renderHome();
      } catch(e) {}
    } else {
      window.location.href = 'index.html';
    }
  });
