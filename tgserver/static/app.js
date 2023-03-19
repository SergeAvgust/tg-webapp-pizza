let tg = window.Telegram.WebApp;

tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37";

let order = {};
let pizzas = {};
let money = 0;

order['user'] = tg.initDataUnsafe.user.username

function incrementSum(amount) {
    money += amount;
    if (money > 0) {
        tg.MainButton.setText(money);
        tg.MainButton.show();
    }
    else {
        tg.MainButton.hide();
    }
};

let inner_btns = document.querySelectorAll('.innerBtns')
inner_btns.forEach(btn_div => {
    let add_btn = btn_div.querySelector('.add');
    let rmv_btn = btn_div.querySelector('.rmv');
    let counter_field = btn_div.querySelector('.counter');
    let counter = 0;

    counter_field.innerHTML = counter;

    add_btn.addEventListener('click', () => {
        counter++;
        counter_field.innerHTML = counter;
        pizzas[btn_div.id] = counter;
        incrementSum(btn_div.querySelector('.price').value)
    });

    rmv_btn.addEventListener('click', () => {
        if (counter > 1) {
            counter--;
            counter_field.innerHTML = counter;
            pizzas[btn_div.id] = counter;
            incrementSum(-btn_div.querySelector('.price').value)
        }
        else if (counter === 1) {
            counter--;
            counter_field.innerHTML = counter;
            delete pizzas[btn_div.id];
            incrementSum(-btn_div.querySelector('.price').value)
        }
    });


});

Telegram.WebApp.onEvent('MainButtonClicked', () => {
    order['pizzas'] = pizzas;
    tg.sendData(order)
})