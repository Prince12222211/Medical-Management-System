// Medical Management System - Advanced Animations & Interactions

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all animations
    initializeAnimations();
    initializeLogoAnimations();
    initializeCounterAnimations();
    initializeParallaxEffects();
    initializeFormAnimations();
    initializeButtonEffects();
    initializeProgressBars();
    initializeScrollAnimations();
    initializeParticleEffect();
    
});

// Initialize general animations
function initializeAnimations() {
    // Add fade-in animation to elements as they come into view
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('.card, .feature-card-animated, .stat-card-animated').forEach(el => {
        observer.observe(el);
    });
}

// Enhanced logo animations
function initializeLogoAnimations() {
    const logos = document.querySelectorAll('.medical-logo');
    
    logos.forEach(logo => {
        logo.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1) rotate(5deg)';
            this.style.filter = 'drop-shadow(0 0 30px rgba(102, 126, 234, 0.8))';
        });
        
        logo.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
            this.style.filter = 'drop-shadow(0 0 10px rgba(102, 126, 234, 0.3))';
        });
        
        // Add click effect
        logo.addEventListener('click', function() {
            this.style.animation = 'none';
            setTimeout(() => {
                this.style.animation = 'logoGlow 2s ease-in-out infinite alternate, pulse 1s ease-in-out';
            }, 10);
        });
    });
}

// Animated counter for statistics
function initializeCounterAnimations() {
    const counters = document.querySelectorAll('[data-counter]');
    
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.getAttribute('data-counter'));
                const duration = 2000;
                const step = target / (duration / 16);
                let current = 0;
                
                const updateCounter = () => {
                    current += step;
                    if (current < target) {
                        counter.textContent = Math.floor(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target;
                    }
                };
                
                updateCounter();
                counterObserver.unobserve(counter);
            }
        });
    });
    
    counters.forEach(counter => counterObserver.observe(counter));
}

// Parallax effects
function initializeParallaxEffects() {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.parallax');
        
        parallaxElements.forEach(element => {
            const speed = element.dataset.speed || 0.5;
            element.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });
}

// Enhanced form animations
function initializeFormAnimations() {
    const inputs = document.querySelectorAll('input, textarea, select');
    
    inputs.forEach(input => {
        // Focus animation
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
            this.style.transform = 'scale(1.02)';
            this.style.boxShadow = '0 0 0 0.25rem rgba(102, 126, 234, 0.25)';
        });
        
        // Blur animation
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
            this.style.transform = 'scale(1)';
            this.style.boxShadow = 'none';
        });
        
        // Input validation animation
        input.addEventListener('input', function() {
            if (this.validity.valid) {
                this.style.borderColor = '#28a745';
                addSuccessIcon(this);
            } else if (this.value.length > 0) {
                this.style.borderColor = '#dc3545';
                addErrorIcon(this);
            }
        });
    });
}

// Add success/error icons to inputs
function addSuccessIcon(input) {
    removeIcons(input);
    const icon = document.createElement('i');
    icon.className = 'bi bi-check-circle-fill text-success input-icon';
    icon.style.cssText = `
        position: absolute;
        right: 10px;
        top: 50%;
        transform: translateY(-50%);
        z-index: 10;
        animation: scaleIn 0.3s ease-out;
    `;
    input.parentElement.style.position = 'relative';
    input.parentElement.appendChild(icon);
}

function addErrorIcon(input) {
    removeIcons(input);
    const icon = document.createElement('i');
    icon.className = 'bi bi-exclamation-circle-fill text-danger input-icon';
    icon.style.cssText = `
        position: absolute;
        right: 10px;
        top: 50%;
        transform: translateY(-50%);
        z-index: 10;
        animation: shake 0.5s ease-in-out;
    `;
    input.parentElement.style.position = 'relative';
    input.parentElement.appendChild(icon);
}

function removeIcons(input) {
    const existingIcons = input.parentElement.querySelectorAll('.input-icon');
    existingIcons.forEach(icon => icon.remove());
}

// Enhanced button effects
function initializeButtonEffects() {
    const buttons = document.querySelectorAll('.btn-animated, .btn');
    
    buttons.forEach(button => {
        // Click ripple effect
        button.addEventListener('click', function(e) {
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            const ripple = document.createElement('span');
            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple 0.6s linear;
                pointer-events: none;
            `;
            
            this.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
        });
        
        // Hover effect enhancement
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.02)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

// Animated progress bars
function initializeProgressBars() {
    const progressBars = document.querySelectorAll('.progress-bar-animated');
    
    const progressObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                const width = bar.getAttribute('data-width') || '100%';
                
                setTimeout(() => {
                    bar.style.width = width;
                }, 200);
                
                progressObserver.unobserve(bar);
            }
        });
    });
    
    progressBars.forEach(bar => progressObserver.observe(bar));
}

// Scroll-triggered animations
function initializeScrollAnimations() {
    const elements = document.querySelectorAll('.scroll-animate');
    
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    });
    
    elements.forEach(el => scrollObserver.observe(el));
}

// Particle effect for hero section
function initializeParticleEffect() {
    const hero = document.querySelector('.hero-section');
    if (!hero) return;
    
    const particlesContainer = document.createElement('div');
    particlesContainer.style.cssText = `
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        overflow: hidden;
    `;
    
    hero.appendChild(particlesContainer);
    
    // Create floating particles
    for (let i = 0; i < 20; i++) {
        createParticle(particlesContainer);
    }
}

function createParticle(container) {
    const particle = document.createElement('div');
    const size = Math.random() * 4 + 2;
    const startX = Math.random() * window.innerWidth;
    const startY = window.innerHeight + 10;
    const duration = Math.random() * 20 + 10;
    const delay = Math.random() * 5;
    
    particle.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        left: ${startX}px;
        top: ${startY}px;
        animation: floatUp ${duration}s ${delay}s infinite linear;
    `;
    
    container.appendChild(particle);
    
    // Remove and recreate particle when animation ends
    setTimeout(() => {
        particle.remove();
        createParticle(container);
    }, (duration + delay) * 1000);
}

// OTP input enhancements
function enhanceOTPInput() {
    const otpInput = document.querySelector('.otp-input-animated');
    if (!otpInput) return;
    
    // Auto-format OTP input
    otpInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/[^0-9]/g, '');
        if (value.length <= 6) {
            e.target.value = value;
            
            // Auto-submit when complete
            if (value.length === 6) {
                setTimeout(() => {
                    const form = e.target.closest('form');
                    if (form) {
                        addLoadingSpinner(form.querySelector('button[type="submit"]'));
                        form.submit();
                    }
                }, 500);
            }
        }
    });
    
    // Add visual feedback for each digit
    otpInput.addEventListener('keydown', function(e) {
        if (e.key >= '0' && e.key <= '9') {
            this.style.animation = 'otpDigitPulse 0.3s ease-out';
            setTimeout(() => {
                this.style.animation = '';
            }, 300);
        }
    });
}

// Loading spinner for buttons
function addLoadingSpinner(button) {
    if (!button) return;
    
    const originalText = button.innerHTML;
    button.innerHTML = '<div class="loading-spinner"></div> Processing...';
    button.disabled = true;
    
    // Remove spinner after timeout (for demo purposes)
    setTimeout(() => {
        button.innerHTML = originalText;
        button.disabled = false;
    }, 3000);
}

// Notification system
function showNotification(message, type = 'info', duration = 5000) {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification-slide`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        border-radius: 15px;
    `;
    notification.innerHTML = `
        <i class="bi bi-${getNotificationIcon(type)}"></i>
        ${message}
        <button type="button" class="btn-close" onclick="this.parentElement.remove()"></button>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        if (notification.parentElement) {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => notification.remove(), 300);
        }
    }, duration);
}

function getNotificationIcon(type) {
    const icons = {
        success: 'check-circle',
        danger: 'exclamation-triangle',
        warning: 'exclamation-circle',
        info: 'info-circle'
    };
    return icons[type] || icons.info;
}

// Enhanced table interactions
function initializeTableAnimations() {
    const tableRows = document.querySelectorAll('tbody tr');
    
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.02)';
            this.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.1)';
            this.style.zIndex = '10';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.boxShadow = 'none';
            this.style.zIndex = '1';
        });
    });
}

// Initialize enhanced features when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    enhanceOTPInput();
    initializeTableAnimations();
    
    // Add CSS animations dynamically
    addCustomAnimations();
});

function addCustomAnimations() {
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple {
            to {
                transform: scale(2);
                opacity: 0;
            }
        }
        
        @keyframes otpDigitPulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        @keyframes floatUp {
            to {
                transform: translateY(-100vh) rotate(360deg);
                opacity: 0;
            }
        }
        
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }
        
        .animate-in {
            animation: slideInUp 0.8s ease-out forwards;
        }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);
}

// Export functions for global use
window.MedicalAnimations = {
    showNotification,
    addLoadingSpinner,
    enhanceOTPInput
};
