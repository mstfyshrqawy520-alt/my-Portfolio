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
  const videoElement = videoModal ? videoModal.querySelector('video') : null;
  const modalClose = videoModal ? videoModal.querySelector('.modal-close') : null;

  document.querySelectorAll('.project-visual').forEach(visual => {
    visual.addEventListener('click', () => {
      const videoSrc = visual.querySelector('source') ? visual.querySelector('source').src : null;
      if (videoSrc && videoModal && videoElement) {
        videoElement.src = videoSrc;
        videoModal.classList.add('active');
        videoElement.play();
      }
    });
  });

  if (modalClose) {
    modalClose.addEventListener('click', () => {
      videoModal.classList.remove('active');
      videoElement.pause();
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
          if (filter === 'all' || card.dataset.category === filter) {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // Info Modal Logic
  const projectData = {
    hiremind: {
      title: 'Hire-Mind — AI Recruitment Intelligence',
      description: 'A production-grade recruitment platform leveraging RAG and semantic search to revolutionize candidate matching.',
      challenges: ['Optimizing semantic search latency.', 'Developing a robust RAG pipeline.', 'Architecting multi-stage AI reasoning.'],
      tech: ['FastAPI', 'LangChain', 'ChromaDB', 'OpenAI', 'Docker'],
      metrics: { 'Acc.': '94%', 'Time Saved': '70%', 'Inference': '2.1s' },
      architecture: '<p>AI Flow: CV Parsing → Vector Embedding → Semantic Search → LLM Ranking.</p>'
    },
    smartdetect: {
      title: 'SmartDetect — Industrial Computer Vision',
      description: 'Real-time multi-stage computer vision pipeline for industrial food quality grading.',
      challenges: ['High-speed inference (60+ FPS).', 'Spatial calibration for size.', 'Environmental variability.'],
      tech: ['PyTorch', 'YOLOv8', 'EfficientNet', 'OpenCV'],
      metrics: { 'FPS': '62', 'mAP': '0.92', 'Latency': '85ms' },
      architecture: '<p>CV Flow: Stream → YOLO Detection → EfficientNet Grading → GUI Output.</p>'
    },
    creditrisk: {
      title: 'Credit Risk Engine — Production ML',
      description: 'Financial risk assessment system with integrated explainability.',
      challenges: ['Imbalanced data handling.', 'SHAP explainability integration.', 'MLflow experiment tracking.'],
      tech: ['Scikit-learn', 'XGBoost', 'SHAP', 'MLflow', 'FastAPI'],
      metrics: { 'AUC': '0.95', 'Precision': '0.88', 'Recall': '0.84' },
      architecture: '<p>ML Flow: Transaction Data → XGBoost → SHAP Explainability → Dashboard.</p>'
    },
    houserent: {
      title: 'House Rent Prediction (ANN)',
      description: 'Deep learning regression model for predicting rental prices.',
      challenges: ['Categorical encoding.', 'Architecture optimization.', 'Overfitting control.'],
      tech: ['TensorFlow', 'Keras', 'Pandas'],
      metrics: { 'R2 Score': '0.89', 'Accuracy': 'High', 'Time': '5m' },
      architecture: '<p>ANN: Input → Dense Layers → Dropout → ReLU → Output.</p>'
    },
    nncollection: {
      title: 'Neural Networks Collection',
      description: 'Comprehensive set of CNN architectures for image classification.',
      challenges: ['Tuning hyperparameters.', 'Comparing CNN vs MLP.', 'Handling MNIST/Fashion-MNIST.'],
      tech: ['PyTorch', 'CNN', 'NumPy'],
      metrics: { 'Accuracy': '99.2%', 'Loss': '0.05', 'Epochs': '20' },
      architecture: '<p>Architecture: Conv2D → MaxPooling → Dense → Softmax.</p>'
    },
    fakenews: {
      title: 'Fake News Detection System',
      description: 'NLP pipeline for detecting misinformation in text.',
      challenges: ['Feature extraction (TF-IDF).', 'Handling sarcasm/nuance.', 'Real-time inference.'],
      tech: ['Scikit-learn', 'NLTK', 'Streamlit'],
      metrics: { 'Accuracy': '93%', 'F1-Score': '0.92', 'Recall': '0.91' },
      architecture: '<p>NLP Flow: Text Clean → TF-IDF → Logistic Regression → Result.</p>'
    },
    captioning: {
      title: 'Image Captioning Systems',
      description: 'Multimodal system generating descriptions from images.',
      challenges: ['Vision-Language alignment.', 'Transformer optimization.', 'Contextual accuracy.'],
      tech: ['ViT', 'GPT-2/BERT', 'PyTorch'],
      metrics: { 'BLEU-4': '0.35', 'METEOR': '0.28', 'CIDEr': '0.95' },
      architecture: '<p>Architecture: ViT Encoder → Cross-Attention → Transformer Decoder.</p>'
    },
    sentiment: {
      title: 'Restaurant Reviews Sentiment',
      description: 'Semantic analysis of customer feedback.',
      challenges: ['Aspect-based sentiment.', 'Domain specific lexicon.', 'Data visualization.'],
      tech: ['TextBlob', 'VADER', 'Matplotlib'],
      metrics: { 'Accuracy': '88%', 'Coverage': '100%', 'Speed': 'Fast' },
      architecture: '<p>Pipeline: Review Text → Sentiment Scoring → Dashboard Visualization.</p>'
    },
    cvfinetuning: {
      title: 'Fine-Tuning CV Models',
      description: 'Transfer learning on industrial datasets.',
      challenges: ['Backbone selection.', 'Freeze/Unfreeze strategy.', 'Dataset augmentation.'],
      tech: ['ResNet', 'ViT', 'TIMM'],
      metrics: { 'mAP': '0.88', 'Top-1 Acc': '91%', 'Size': '224px' },
      architecture: '<p>Process: Pretrained Weights → Custom Head → Layer Tuning → Final Model.</p>'
    },
    nlpdashboard: {
      title: 'HuggingFace AI Dashboard',
      description: 'Interactive NLP multi-tool using Gradio.',
      challenges: ['Multiple model integration.', 'Gradio UI responsiveness.', 'Latency management.'],
      tech: ['Gradio', 'Transformers', 'HuggingFace'],
      metrics: { 'Tasks': '5+', 'Models': '10+', 'Uptime': '99%' },
      architecture: '<p>Stack: HuggingFace API → Gradio Interface → Deployment.</p>'
    },
    llmfinetuning: {
      title: 'Fine-Tuning GPT (LLM)',
      description: 'Instruction tuning for specialized tasks.',
      challenges: ['Dataset preparation.', 'PEFT/LoRA optimization.', 'Memory constraints (VRAM).'],
      tech: ['LoRA', 'QLoRA', 'OpenAI API'],
      metrics: { 'Ctx length': '8k', 'Tuning Time': '12h', 'Eval': 'High' },
      architecture: '<p>Workflow: Raw Text → Alpaca Format → QLoRA Tuning → Merged Model.</p>'
    },
    ttsaudio: {
      title: 'TTS & Audio Generation',
      description: 'Natural voice synthesis systems.',
      challenges: ['Prosody and emotion.', 'Vocoder selection.', 'Inference speed.'],
      tech: ['FastSpeech', 'HiFi-GAN', 'Librosa'],
      metrics: { 'MOS': '4.2', 'Speed': 'Real-time', 'Lang': 'Multilingual' },
      architecture: '<p>Audio Flow: Text → Mel-spectrogram → Vocoder → Waveform.</p>'
    },
    gamedesigner: {
      title: 'AI Game Character Designer',
      description: 'Generative art tool for character assets.',
      challenges: ['Consistency in style.', 'ControlNet implementation.', 'Prompt engineering.'],
      tech: ['Stable Diffusion', 'Gradio', 'Lora'],
      metrics: { 'Gen Time': '5s', 'Style Match': '95%', 'Resolution': '1024px' },
      architecture: '<p>Creative Flow: Prompt → Latent Diffusion → Upscaling → Character Sheet.</p>'
    },
    ganfromscratch: {
      title: 'GAN from Scratch',
      description: 'Custom GAN implementation for synthetic data.',
      challenges: ['Mode collapse.', 'Generator/Discriminator balance.', 'Loss stability.'],
      tech: ['PyTorch', 'NumPy', 'CNN'],
      metrics: { 'FID Score': '低', 'Epochs': '100+', 'Stability': 'Good' },
      architecture: '<p>GAN Flow: Noise → Generator → Synthetic Image ↔ Discriminator ↔ Real Image.</p>'
    },
    genai: {
      title: 'Generative AI Pillar',
      description: 'Expertise in modern generative systems.',
      challenges: ['RAG optimization.', 'Multi-agent coordination.', 'Prompt stability.'],
      tech: ['LangChain', 'CrewAI', 'GPT-4o'],
      metrics: { 'Context': '128k', 'Precision': '96%', 'Cost': '-40%' },
      architecture: '<p>Domain: Agentic Workflows & Knowledge Retrieval.</p>'
    },
    cv_domain: {
      title: 'Vision Intelligence Pillar',
      description: 'Industrial vision applications.',
      challenges: ['Real-time processing.', 'Edge deployment.', 'High accuracy.'],
      tech: ['YOLOv8', 'PyTorch', 'EfficientNet'],
      metrics: { 'FPS': '60+', 'mAP': '0.92', 'Latency': '<50ms' },
      architecture: '<p>Domain: Detection, Classification & Tracking.</p>'
    },
    mlops_eng: {
      title: 'MLOps & AI Engineering Pillar',
      description: 'Scaling AI to production.',
      challenges: ['CI/CD for ML.', 'Model monitoring.', 'Reproducibility.'],
      tech: ['Docker', 'MLflow', 'AWS'],
      metrics: { 'Uptime': '99.9%', 'Scale': 'TB+', 'Deploy': 'Auto' },
      architecture: '<p>Domain: Infrastructure & Lifecycle Management.</p>'
    }
  };

  const infoModal = document.getElementById('info-modal');
  const infoContent = document.getElementById('project-details-content');
  const infoClose = document.getElementById('info-modal-close');

  const setupModalBtns = () => {
    document.querySelectorAll('.project-more-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const project = projectData[btn.dataset.project];
        if (project) {
          infoContent.innerHTML = `
            <h2 style="margin-bottom: 1.5rem; color: var(--accent); font-size: 2.5rem;">${project.title}</h2>
            <div style="margin-bottom: 2rem; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;">
              ${Object.entries(project.metrics).map(([name, value]) => `
                <div style="background: rgba(255,255,255,0.03); padding: 1rem; border-radius: 12px; text-align: center; border: 1px solid var(--border);">
                  <p style="font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase;">${name}</p>
                  <p style="font-size: 1.2rem; font-weight: 700; color: var(--accent);">${value}</p>
                </div>
              `).join('')}
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
              <div>
                <h4 style="color: var(--text-primary); margin-bottom: 0.5rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem;">Key Challenges</h4>
                <ul style="color: var(--text-secondary); padding-left: 1.2rem; line-height: 1.6; font-size: 0.9rem;">
                  ${project.challenges.map(c => `<li style="margin-bottom: 0.8rem;">${c}</li>`).join('')}
                </ul>
                <h4 style="color: var(--text-primary); margin-top: 1.5rem; margin-bottom: 0.5rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem;">Tech Stack</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.8rem;">
                  ${project.tech.map(t => `<span class="tag" style="font-size: 0.7rem; padding: 0.2rem 0.5rem;">${t}</span>`).join('')}
                </div>
              </div>
              <div>
                <h4 style="color: var(--text-primary); margin-bottom: 0.5rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem;">Pipeline Architecture</h4>
                ${project.architecture}
              </div>
            </div>
          `;
          infoModal.classList.add('active');
        }
      });
    });
  };

  setupModalBtns();

  if (infoClose) {
    infoClose.addEventListener('click', () => infoModal.classList.remove('active'));
  }

  window.addEventListener('click', (e) => {
    if (e.target === infoModal) infoModal.classList.remove('active');
  });

  // Chatbot Logic
  const chatBubble = document.getElementById('chat-bubble');
  const chatWindow = document.getElementById('chat-window');
  if (chatBubble) {
    chatBubble.addEventListener('click', () => chatWindow.classList.toggle('active'));
  }

  const responses = {
    "Who is Mostafa?": "Mostafa Elsharqawi is a high-honors (A+) AI/ML Engineer specializing in building end-to-end intelligent systems. He has deep expertise in LLMs, RAG pipelines, and Computer Vision. <br><br><a href='#about' style='color:var(--accent); text-decoration:underline;'>Learn more about my background →</a>",
    "View Featured Projects": "Mostafa's flagship projects include: <br>1. <a href='https://github.com/mstfyshrqawy520-alt/HireMind-AI-Recruitment-System' target='_blank' style='color:var(--accent);'>**Hire-Mind AI**</a> (RAG)<br>2. <a href='https://github.com/mstfyshrqawy520-alt/FruitGuard-System' target='_blank' style='color:var(--accent);'>**SmartDetect CV**</a> (Vision)<br>3. <a href='https://github.com/mstfyshrqawy520-alt/credit-risk-engine-main-ML-' target='_blank' style='color:var(--accent);'>**Credit Risk Engine**</a> (ML).",
    "Technical Skills": "Mostafa is an expert in **Python, PyTorch, and TensorFlow**. His core stack includes **LangChain, CrewAI, YOLOv8, and MLOps tools**. <br><br><a href='#skills' style='color:var(--accent); text-decoration:underline;'>View full technical stack →</a>",
    "How to Contact?": "You can reach Mostafa via:<br>📧 <a href='mailto:mstfyshrqawy520@gmail.com' style='color:var(--accent);'>**Email Me**</a><br>🔗 <a href='https://linkedin.com/in/mostafa-el-sharqawi-66b3a7352' target='_blank' style='color:var(--accent);'>**LinkedIn Profile**</a><br>💻 <a href='https://github.com/mstfyshrqawy520-alt' target='_blank' style='color:var(--accent);'>**GitHub Portfolio**</a>"
  };

  const chatBody = document.getElementById('chat-body');
  document.querySelectorAll('.opt-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const msg = btn.dataset.msg;
      
      // Add User Message
      const userMsg = document.createElement('div');
      userMsg.className = 'chat-message user';
      userMsg.textContent = msg;
      chatBody.appendChild(userMsg);

      // Add Bot Response
      setTimeout(() => {
        const botMsg = document.createElement('div');
        botMsg.className = 'chat-message bot';
        botMsg.innerHTML = responses[msg] || "I'm sorry, I don't have a specific answer for that yet. Feel free to contact Mostafa directly!";
        chatBody.appendChild(botMsg);
        chatBody.scrollTop = chatBody.scrollHeight;
      }, 600);
    });
  });

  // Scroll Progress Logic
  window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    const progress = document.getElementById('scroll-progress');
    if (progress) progress.style.width = scrolled + "%";
  });

  // Copy Email Logic
  const emailLink = document.querySelector('a[href^="mailto"]');
  if (emailLink) {
    emailLink.addEventListener('click', (e) => {
      const email = "mstfyshrqawy520@gmail.com";
      navigator.clipboard.writeText(email).then(() => {
        const toast = document.createElement('div');
        toast.style.cssText = "position:fixed; bottom:20px; right:20px; background:var(--accent); color:black; padding:10px 20px; border-radius:10px; z-index:10000; font-weight:600; animation: fadeInUp 0.3s ease;";
        toast.textContent = "Email copied to clipboard!";
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 3000);
      });
    });
  }

  // Skills Tab Logic
  const skillTabs = document.querySelectorAll('.tab-btn');
  const skillCategories = document.querySelectorAll('.skills-category');

  if (skillTabs.length > 0 && skillCategories.length > 0) {
    skillTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        // Remove active class from all tabs
        skillTabs.forEach(t => t.classList.remove('active'));
        // Add active class to clicked tab
        tab.classList.add('active');

        // Hide all categories
        skillCategories.forEach(cat => cat.classList.remove('active'));
        // Show selected category
        const targetCategory = tab.dataset.category;
        const targetEl = document.getElementById(targetCategory);
        if (targetEl) {
          targetEl.classList.add('active');
        }
      });
    });
  }
  // FAQ Accordion Logic
  const faqItems = document.querySelectorAll('.faq-item');
  if (faqItems.length > 0) {
    faqItems.forEach(item => {
      const question = item.querySelector('.faq-question');
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        
        // Close all other items
        faqItems.forEach(i => i.classList.remove('active'));
        
        // Toggle current item
        if (!isActive) {
          item.classList.add('active');
        }
      });
    });
  }
});