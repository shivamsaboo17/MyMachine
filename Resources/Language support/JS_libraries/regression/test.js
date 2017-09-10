var regression = require("regression");
var dataString = `2104,399900
1600,329900
2400,369000
1416,232000
3000,539900
1985,299900
1534,314900
1427,198999
1380,212000
1494,242500
1940,239999
2000,347000
1890,329999
4478,699900
1268,259900
2300,449900
1320,299900
1236,199900
2609,499998
3031,599000
1767,252900
1888,255000
1604,242900
1962,259900
3890,573900
1100,249900
1458,464500
2526,469000
2200,475000
2637,299900
1839,349900
1000,169900
2040,314900
3137,579900
1811,285900
1437,249900
1239,229900
2132,345000
4215,549000
2162,287000
1664,368500
2238,329900
2567,314000
1200,299000
852,179900
1852,299900
1203,239500`
var rawdata = dataString.split("\n");
  // console.log(data[0]);
  // data = parseInt(data);
  // console.log(data[0]);
var temp;
var dataset = [];

for (var i = 0; i < rawdata.length; i++) {
 temp = rawdata[i].split(",");
 // dataset.push(temp);
 // dataset[i] = temp;
 temp[0] = parseInt(temp[0]);
 temp[1] = parseInt(temp[1]);
 dataset.push(temp);

}


console.log(`the following is the dataset that I've used here ${dataset}`);
const result = regression.linear(dataset);
const gradient = result.equation[0];
const yIntercept = result.equation[1];

console.log(`the equation for linear regression is :\n y = ${gradient}x + ${yIntercept}`);





var pres = regression.polynomial(dataset, { order: 3 });

// console.log(pres);
console.log(`the given equation is: ${pres.string}`);
console.log(`prediction for x = 1372 is: ${pres.predict(1372)}`);



// the following is the code for exponential regression

var eres = regression.exponential(dataset, {order: 2});
// console.log(eres);
console.log(`the given equation is: ${eres.string}`);
console.log(`prediction for x = 1372 is: ${eres.predict(1372)}`);


//the following is the code for logarithmic regression
var lres = regression.logarithmic(dataset, {order: 2});
// console.log(lres);
console.log(`the given equation is: ${lres.string}`);
console.log(`prediction for x = 1372 is: ${lres.predict(1372)}`);


//the following is the code for logarithmic regressionp
var pres = regression.power(dataset, {order: 2});
// console.log(lres);
console.log(`the given equation is: ${pres.string}`);
console.log(`prediction for x = 1372 is: ${pres.predict(1372)}`);
