document.addEventListener('DOMContentLoaded', () => {
  // Reveal animations
  const reveal = () => {
    const reveals = document.querySelectorAll('.reveal');
    reveals.forEach(el => {
      const windowHeight = window.innerHeight;
      const elementTop = el.getBoundingClientRect().top;
      const elementVisible = 150;
      if (elementTop < windowHeight - elementVisible) {
        el.classList.add('active');
      }
    });
  };

  window.addEventListener('scroll', reveal);
  reveal(); // Initial check

  // Video Modal Logic
  const videoModal = document.getElementById('video-modal');
  const modalContainer = videoModal ? videoModal.querySelector('.modal-content') : null;
  const modalClose = videoModal ? videoModal.querySelector('.modal-close') : null;

  document.querySelectorAll('.project-visual').forEach(visual => {
    visual.addEventListener('click', () => {
      const youtubeId = visual.dataset.youtube;
      const videoSrc = visual.querySelector('source') ? visual.querySelector('source').src : null;
      
      if (videoModal && modalContainer) {
        const closeBtn = modalContainer.querySelector('.modal-close');
        modalContainer.innerHTML = '';
        modalContainer.appendChild(closeBtn);

        if (youtubeId) {
          const iframe = document.createElement('iframe');
          iframe.src = `https://www.youtube.com/embed/${youtubeId}?autoplay=1`;
          iframe.setAttribute('allowfullscreen', '');
          iframe.setAttribute('allow', 'autoplay; encrypted-media');
          iframe.style.width = '100%';
          iframe.style.aspectRatio = '16/9';
          iframe.style.borderRadius = '12px';
          iframe.style.border = 'none';
          modalContainer.appendChild(iframe);
        } else if (videoSrc) {
          const video = document.createElement('video');
          video.src = videoSrc;
          video.controls = true;
          video.autoplay = true;
          video.style.width = '100%';
          video.style.borderRadius = '12px';
          modalContainer.appendChild(video);
        }
        videoModal.classList.add('active');
      }
    });
  });

  if (modalClose) {
    modalClose.addEventListener('click', () => {
      videoModal.classList.remove('active');
      if (modalContainer) {
        const closeBtn = modalContainer.querySelector('.modal-close');
        modalContainer.innerHTML = '';
        modalContainer.appendChild(closeBtn);
      }
    });
  }

  // Certifications Slider
  const gallery = document.getElementById('cert-gallery');
  const prevBtn = document.getElementById('cert-prev');
  const nextBtn = document.getElementById('cert-next');
  const filterBtns = document.querySelectorAll('.filter-btn');

  if (gallery && prevBtn && nextBtn) {
    nextBtn.addEventListener('click', () => {
      gallery.scrollBy({ left: 300, behavior: 'smooth' });
    });
    prevBtn.addEventListener('click', () => {
      gallery.scrollBy({ left: -300, behavior: 'smooth' });
    });
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;
        document.querySelectorAll('.cert-card').forEach(card => {
          card.style.display = (filter === 'all' || card.dataset.category === filter) ? 'block' : 'none';
        });
      });
    });
  }

  // Info Modal Logic
  const projectData = {
    localgpt: {
      title: 'LocalGPT — Private Document Intelligence',
      description: 'An advanced AI platform for private document analysis locally.',
      challenges: ['Data privacy', 'Hybrid search', 'LLM integration'],
      tech: ['Next.js', 'FastAPI', 'Ollama', 'LanceDB'],
      metrics: { 'Privacy': '100%', 'Retrieval': 'Hybrid', 'Deployment': 'Local' },
      architecture: '<p>System: Next.js Frontend ↔ FastAPI Backend ↔ RAG Pipeline ↔ Ollama.</p>'
    },
    hiremind: {
      title: 'Hire-Mind — AI Recruitment Intelligence',
      description: 'Production-grade recruitment platform using RAG.',
      challenges: ['Latency optimization', 'RAG pipeline', 'AI reasoning'],
      tech: ['FastAPI', 'LangChain', 'ChromaDB', 'OpenAI'],
      metrics: { 'Acc.': '94%', 'Time Saved': '70%', 'Inference': '2.1s' },
      architecture: '<p>AI Flow: CV Parsing → Vector Embedding → Semantic Search → LLM Ranking.</p>'
    },
    smartdetect: {
      title: 'SmartDetect — Industrial CV',
      description: 'Real-time multi-stage CV pipeline.',
      challenges: ['High-speed inference', 'Spatial calibration', 'Variability'],
      tech: ['PyTorch', 'YOLOv8', 'EfficientNet', 'OpenCV'],
      metrics: { 'FPS': '62', 'mAP': '0.92', 'Latency': '85ms' },
      architecture: '<p>CV Flow: Stream → YOLO Detection → EfficientNet Grading → Output.</p>'
    },
    creditrisk: {
      title: 'Credit Risk Engine — Production ML',
      description: 'Financial risk assessment system with explainability.',
      challenges: ['Imbalanced data', 'SHAP integration', 'MLflow tracking'],
      tech: ['Scikit-learn', 'XGBoost', 'SHAP', 'MLflow', 'FastAPI'],
      metrics: { 'AUC': '0.95', 'Precision': '0.88', 'Recall': '0.84' },
      architecture: '<p>ML Flow: Transaction Data → XGBoost → SHAP Explainability → Dashboard.</p>'
    },
    houserent: {
      title: 'House Rent Prediction (ANN)',
      description: 'Deep learning regression model for predicting rental prices.',
      challenges: ['Categorical encoding', 'Architecture optimization', 'Overfitting control'],
      tech: ['TensorFlow', 'Keras', 'Pandas', 'FastAPI'],
      metrics: { 'R2 Score': '0.89', 'Accuracy': 'High', 'Latency': 'Real-time' },
      architecture: '<p>ANN: Input → Dense Layers → Dropout → ReLU → Output.</p>'
    },
    breastcancer: {
      title: 'Breast Cancer Detection Assistance',
      description: 'High-precision diagnostic tool for breast cancer classification.',
      challenges: ['Diagnostic accuracy', 'Secure API', 'Clinical interface'],
      tech: ['Scikit-learn', 'FastAPI', 'Streamlit'],
      metrics: { 'Accuracy': '97%+', 'Inference': '50ms', 'Precision': 'High' },
      architecture: '<p>Workflow: Input → Preprocessing → Random Forest → Diagnostic Output.</p>'
    },
    glioma: {
      title: 'Glioma Tumor Grading',
      description: 'Clinical support system for grading brain tumors.',
      challenges: ['Imbalanced datasets', 'Genetic markers', 'Usability'],
      tech: ['Scikit-learn', 'SMOTE', 'Streamlit'],
      metrics: { 'F1-Score': '0.94', 'Recall': '0.92', 'Latency': 'Real-time' },
      architecture: '<p>Workflow: Genetic Markers → SMOTE Balancing → Ensemble Classifier → Grade Prediction.</p>'
    },
    grapeleaf: {
      title: 'Grape Leaves Disease Identification',
      description: 'CV system using ResNet50 for disease detection.',
      challenges: ['Dataset noise', 'Transfer Learning', 'UI ready'],
      tech: ['TensorFlow', 'ResNet50', 'OpenCV', 'FastAPI'],
      metrics: { 'Accuracy': '96%', 'Resolution': '224px', 'Inference': '120ms' },
      architecture: '<p>CV Flow: Image Upload → ResNet50 → Dense Classifier → Disease Label.</p>'
    },
    fakenews: {
      title: 'Fake News Authenticity Verifier',
      description: 'NLP pipeline for verifying news authenticity.',
      challenges: ['Linguistic nuances', 'TF-IDF dimensionality', 'Processing speed'],
      tech: ['NLTK', 'Scikit-learn', 'Logistic Regression', 'Streamlit'],
      metrics: { 'Accuracy': '89%', 'Processing': 'Secs', 'Language': 'English' },
      architecture: '<p>NLP Flow: Raw Text → Cleaning (Lemmatization) → TF-IDF → Logistic Regression → Result.</p>'
    }
  };

  const infoModal = document.getElementById('info-modal');
  const infoContent = document.getElementById('project-details-content');
  const infoClose = document.getElementById('info-modal-close');

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.project-more-btn');
    if (btn && infoModal && infoContent) {
      const projectId = btn.dataset.project;
      const data = projectData[projectId];
      if (data) {
        let techHtml = data.tech.map(t => `<span class="tag">${t}</span>`).join('');
        let challengeHtml = data.challenges.map(c => `<li>${c}</li>`).join('');
        let metricsHtml = Object.entries(data.metrics).map(([k, v]) => `
          <div class="metric-item">
            <span class="metric-val">${v}</span>
            <span class="metric-label">${k}</span>
          </div>
        `).join('');

        infoContent.innerHTML = `
          <div class="modal-header"><h3>${data.title}</h3></div>
          <div class="modal-body">
            <div class="modal-section"><h4>Overview</h4><p>${data.description}</p></div>
            <div class="modal-section"><h4>Tech Stack</h4><div class="project-tags">${techHtml}</div></div>
            <div class="modal-grid">
              <div class="modal-section"><h4>Key Challenges</h4><ul class="modal-list">${challengeHtml}</ul></div>
              <div class="modal-section"><h4>Performance</h4><div class="metrics-grid">${metricsHtml}</div></div>
            </div>
            <div class="modal-section"><h4>System Architecture</h4><div class="architecture-flow">${data.architecture}</div></div>
          </div>
        `;
        infoModal.classList.add('active');
      }
    }
  });

  if (infoClose) infoClose.addEventListener('click', () => infoModal.classList.remove('active'));
  window.addEventListener('click', (e) => { if (e.target === infoModal) infoModal.classList.remove('active'); });

  // Chatbot Logic
  const chatBubble = document.getElementById('chat-bubble');
  const chatWindow = document.getElementById('chat-window');
  if (chatBubble) chatBubble.addEventListener('click', () => chatWindow.classList.toggle('active'));

  const responses = {
    "Who is Mostafa?": "Mostafa Elsharqawi is a high-honors AI/ML Engineer specializing in LLMs, RAG, and CV.",
    "View Featured Projects": "Key projects: Hire-Mind AI, SmartDetect CV, Credit Risk Engine.",
    "Technical Skills": "Expert in Python, PyTorch, TensorFlow, LangChain, and YOLOv8.",
    "How to Contact?": "Email: mstfyshrqawy520@gmail.com | LinkedIn: mostafa-el-sharqawi-66b3a7352"
  };

  const chatBody = document.getElementById('chat-body');
  document.querySelectorAll('.opt-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const msg = btn.dataset.msg;
      const userMsg = document.createElement('div');
      userMsg.className = 'chat-message user';
      userMsg.textContent = msg;
      chatBody.appendChild(userMsg);
      setTimeout(() => {
        const botMsg = document.createElement('div');
        botMsg.className = 'chat-message bot';
        botMsg.innerHTML = responses[msg] || "I'll get back to you soon!";
        chatBody.appendChild(botMsg);
        chatBody.scrollTop = chatBody.scrollHeight;
      }, 600);
    });
  });

  // Scroll Progress
  window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    const progress = document.getElementById('scroll-progress');
    if (progress) progress.style.width = scrolled + "%";
  });

  // Copy Email
  const emailLink = document.querySelector('a[href^="mailto"]');
  if (emailLink) {
    emailLink.addEventListener('click', (e) => {
      navigator.clipboard.writeText("mstfyshrqawy520@gmail.com").then(() => {
        const toast = document.createElement('div');
        toast.style.cssText = "position:fixed; bottom:20px; right:20px; background:var(--accent); color:black; padding:10px 20px; border-radius:10px; z-index:10000; font-weight:600;";
        toast.textContent = "Email copied!";
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 3000);
      });
    });
  }

  // Skills Tabs
  const skillTabs = document.querySelectorAll('.tab-btn');
  const skillCategories = document.querySelectorAll('.skills-category');
  skillTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      skillTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      skillCategories.forEach(cat => cat.classList.remove('active'));
      const target = document.getElementById(tab.dataset.category);
      if (target) target.classList.add('active');
    });
  });

  // FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    item.querySelector('.faq-question').addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      faqItems.forEach(i => i.classList.remove('active'));
      if (!isActive) item.classList.add('active');
    });
  });
});