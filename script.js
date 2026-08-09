// DOM Elements
const publicView = document.getElementById('public-view');
const studentPortal = document.getElementById('student-portal');

// Pricing Data for dynamic branching
const pricingData = {
    jordan: {
        currency: 'JOD',
        price1: '45',
        price2: '120',
        subtitle: 'نعرض حالياً الأسعار لفرع <strong class="text-accent">الأردن</strong>'
    },
    palestine: {
        currency: 'ILS', // Assuming Shekel or USD based on PDF (تُحدد لاحقاً (شيكل / دولار))
        price1: '250',
        price2: '650',
        subtitle: 'نعرض حالياً الأسعار لفرع <strong class="text-accent">فلسطين</strong>'
    }
};

// Toggle between Public Website and Student Portal
function togglePortal() {
    if (publicView.classList.contains('hidden')) {
        // Show Public
        publicView.classList.remove('hidden');
        studentPortal.classList.add('hidden');
        window.scrollTo(0, 0);
    } else {
        // Show Portal
        publicView.classList.add('hidden');
        studentPortal.classList.remove('hidden');
    }
}

// Handle Branch Selection for Pricing
function setBranch(branchName) {
    // Update active button state
    document.querySelectorAll('.branch-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    // Update pricing DOM
    const data = pricingData[branchName];
    
    document.getElementById('pricing-subtitle').innerHTML = data.subtitle;
    
    // Animate price change
    const priceElements = [
        { c: 'curr-1', p: 'price-1', v: data.price1 },
        { c: 'curr-2', p: 'price-2', v: data.price2 }
    ];

    priceElements.forEach(item => {
        const pEl = document.getElementById(item.p);
        pEl.style.opacity = 0;
        setTimeout(() => {
            document.getElementById(item.c).textContent = data.currency;
            pEl.textContent = item.v;
            pEl.style.opacity = 1;
        }, 300);
    });
}

// Add smooth scrolling to public navbar
document.querySelectorAll('.nav-links a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        // Remove active class from all
        document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
        // Add to current
        this.classList.add('active');

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
