// src/api/apiService.js
const BASE_URL = "http://20.244.56.144/test/companies";

export const fetchProducts = async (company, category, minPrice, maxPrice) => {
    const response = await fetch(`${BASE_URL}/${company}/categories/${category}/products?minPrice=${minPrice}&maxPrice=${maxPrice}`);
    const data = await response.json();
    return data;
};
