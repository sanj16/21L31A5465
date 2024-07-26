// src/utils/generateUniqueId.js
const generateUniqueId = (product) => {
    return `${product.productName}-${product.price}-${product.rating}-${Math.random()}`;
};

export default generateUniqueId;
