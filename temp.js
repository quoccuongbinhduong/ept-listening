
    let userToken = null;
    let fullData = null;
    let currentTest = "1";
    let userAnswers = {};
    let isSubmitted = false;

    async function checkAuth() {
      const stored = localStorage.getItem('ept_auth');
      if (stored) {
        userToken = stored;
        document.getElementById('user-display').innerText = userToken;
        loadData();
      } else {
        window.location.href = 'index.html';
      }
    }

    async function loadData() {
      try {
        const res = await fetch('reading_data.json?t=' + Date.now());
        fullData = await res.json();
        changeTest("1");
      } catch(e) {
        console.error("Error loading reading data", e);
      }
    }

    function changeTest(testId) {
      if (!fullData || !fullData[testId]) return;
      currentTest = testId;
      isSubmitted = false;
      userAnswers = {};
      
      const testInfo = fullData[testId];
      
      // Update PDF Viewer
      document.getElementById('pdf-viewer').src = `${testInfo.file}#toolbar=0&navpanes=0&scrollbar=1`;
      
      // Render Bubble Sheet (101 to 200)
      const container = document.getElementById('bubble-sheet');
      container.innerHTML = '';
      
      // We assume 100 questions from 101 to 200
      for(let qnum=101; qnum<=200; qnum++) {
        const qnumStr = qnum.toString();
        // Skip if this test doesn't have an answer for this question in the DB (just a safety check)
        if (!testInfo.answers[qnumStr]) continue;
        
        let rowHtml = `<div class="q-row" id="row-${qnumStr}">
          <div class="q-num">${qnumStr}.</div>
          <div class="q-opts">`;
          
        ['A','B','C','D'].forEach(letter => {
          rowHtml += `<div class="q-opt" id="opt-${qnumStr}-${letter}" onclick="selectOption('${qnumStr}', '${letter}')">${letter}</div>`;
        });
        
        rowHtml += `</div></div>`;
        
        // Add explanation box if it exists
        const exp = testInfo.explanations && testInfo.explanations[qnumStr];
        const trans = testInfo.translations && testInfo.translations[qnumStr];
        
        let expHtml = '';
        if (exp || trans) {
          expHtml += `<div class="exp-box" id="exp-${qnumStr}">`;
          if (trans) expHtml += `<div class="trans"><b>Dịch:</b> ${trans}</div>`;
          if (exp) expHtml += `<div><b>Giải thích:</b> ${exp}</div>`;
          expHtml += `</div>`;
        }
        
        container.insertAdjacentHTML('beforeend', rowHtml + expHtml);
      }
      
      document.getElementById('submit-btn').classList.remove('hidden');
    }

    function selectOption(qnum, letter) {
      if (isSubmitted) return;
      userAnswers[qnum] = letter;
      
      ['A','B','C','D'].forEach(l => {
        const el = document.getElementById(`opt-${qnum}-${l}`);
        if(el) el.classList.remove('sel');
      });
      document.getElementById(`opt-${qnum}-${letter}`).classList.add('sel');
    }

    async function submitTest() {
      if (!confirm("Bạn có chắc chắn muốn nộp bài?")) return;
      isSubmitted = true;
      document.getElementById('submit-btn').classList.add('hidden');

      const testInfo = fullData[currentTest];
      let score = 0;
      let total = 0;
      
      Object.keys(testInfo.answers).forEach(qnum => {
        total++;
        const correct = testInfo.answers[qnum];
        const userAns = userAnswers[qnum];
        
        if (userAns) {
          if (userAns === correct) {
            document.getElementById(`opt-${qnum}-${userAns}`).classList.add('ok');
            score++;
          } else {
            document.getElementById(`opt-${qnum}-${userAns}`).classList.add('no');
            document.getElementById(`opt-${qnum}-${correct}`).classList.add('ok');
          }
        } else {
          document.getElementById(`opt-${qnum}-${correct}`).classList.add('ok');
        }

        // Show explanation if exists
        const expEl = document.getElementById(`exp-${qnum}`);
        if (expEl) expEl.classList.add('show');
      });

      alert(`Bạn đã làm đúng ${score}/${total} câu!`);
      
      // Save progress
      if (userToken) {
        /*
        fetch('/api/sync', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            user: userToken,
            app: 'reading_' + currentTest,
            state: { score, total, answers: userAnswers, timestamp: Date.now() }
          })
        });
        */
      }
    }

    checkAuth();
  