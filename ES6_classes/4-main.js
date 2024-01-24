import Pricing from './4-pricing.js';
import Currency from './3-currency.js';

const p = new Pricing(100, new Currency('EUR', 'Euro'));
const po = new Pricing(200, )
console.log(p.amount);
console.log(p.displayFullPrice());
