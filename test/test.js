const hashing = require("..")

let data = new Buffer.from("7000000001e980924e4e1109230383e66d62945ff8e749903bea4336755c00000000000051928aff1b4d72416173a8c3948159a09a73ac3bb556aa6bfbcad1a85da7f4c1d13350531e24031b939b9e2b", "hex");
console.log(hashing);

let hashedData = hashing.hash(data);
console.log(hashedData);