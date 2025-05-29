class CartNotification extends HTMLElement {
  constructor() {
    super();

    this.notification = document.getElementById('cart-notification');
    this.header = document.querySelector('sticky-header');
    this.onBodyClick = this.handleBodyClick.bind(this);

    this.notification.addEventListener('keyup', (evt) => evt.code === 'Escape' && this.close());
    this.querySelectorAll('button[type="button"]').forEach((closeButton) =>
      closeButton.addEventListener('click', this.close.bind(this))
    );
  }

  open() {
    this.notification.classList.add('animate', 'active');

    this.notification.addEventListener('transitionend', () => {
      this.notification.focus();
      trapFocus(this.notification);
    }, { once: true });

    document.body.addEventListener('click', this.onBodyClick);
  }

  close() {
    this.notification.classList.remove('active');

    document.body.removeEventListener('click', this.onBodyClick);

    removeTrapFocus(this.activeElement);
  }

  renderContents(parsedState) {
      this.cartItemKey = parsedState.key;
      this.getSectionsToRender().forEach((section => {
        document.getElementById(section.id).innerHTML =
          this.getSectionInnerHTML(parsedState.sections[section.id], section.selector);
      }));

      if (this.header) this.header.reveal();
      this.open();
  }

  getSectionsToRender() {
    return [
      {
        id: 'cart-notification-product',
        selector: `[id="cart-notification-product-${this.cartItemKey}"]`,
      },
      {
        id: 'cart-notification-button'
      },
      {
        id: 'cart-icon-bubble'
      }
    ];
  }

  getSectionInnerHTML(html, selector = '.shopify-section') {
    return new DOMParser()
      .parseFromString(html, 'text/html')
      .querySelector(selector).innerHTML;
  }

  handleBodyClick(evt) {
    const target = evt.target;
    if (target !== this.notification && !target.closest('cart-notification')) {
      const disclosure = target.closest('details-disclosure, header-menu');
      this.activeElement = disclosure ? disclosure.querySelector('summary') : null;
      this.close();
    }
  }

  setActiveElement(element) {
    this.activeElement = element;
  }
}

customElements.define('cart-notification', CartNotification);
(function () {
    if (sessionStorage.getItem("noticeClosed")) return;
  
    const noticeBar = document.createElement("div");
    noticeBar.style.position = "relative";
    noticeBar.style.backgroundColor = "rgb(0, 140, 255)";
    noticeBar.style.color = "#ffffff";
    noticeBar.style.padding = "10px 20px";
    noticeBar.style.fontSize = "16px";
    noticeBar.style.textAlign = "center";
    noticeBar.style.boxShadow = "0 2px 4px rgba(0,0,0,0.1)";
    noticeBar.style.zIndex = "9999";
  
    // Message wrapper to center
    const messageWrapper = document.createElement("div");
    messageWrapper.innerHTML = "Buy this aged domain and original website togather (2 in 1) — now available at a highly affordable price on <a href='https://age.domains' target='_blank' style='color: inherit; text-decoration: underline;'>age.domains</a>!";
    messageWrapper.style.maxWidth = "100%";
    messageWrapper.style.margin = "0 auto";
    messageWrapper.style.display = "inline-block";
    
    noticeBar.appendChild(messageWrapper);
  
    // Close button
    const closeBtn = document.createElement("button");
    closeBtn.textContent = "×";
    closeBtn.style.position = "absolute";
    closeBtn.style.top = "50%";
    closeBtn.style.right = "-0.1%";
    closeBtn.style.transform = "translateY(-50%)";
    closeBtn.style.background = "none";
    closeBtn.style.border = "none";
    closeBtn.style.fontSize = "20px";
    closeBtn.style.cursor = "pointer";
    closeBtn.style.color = "#ffffff";
    closeBtn.onclick = function () {
      noticeBar.remove();
      sessionStorage.setItem("noticeClosed", "true");
    };
  
    noticeBar.appendChild(closeBtn);
  
    window.addEventListener("DOMContentLoaded", function () {
      const masthead = document.getElementById("masthead");
      if (masthead && masthead.parentNode) {
        masthead.parentNode.insertBefore(noticeBar, masthead);
      } else {
        document.body.prepend(noticeBar);
      }
    });
  })();
  
