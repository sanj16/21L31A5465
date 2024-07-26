// src/pages/AllProductsPage.js
import React, { useState, useEffect } from 'react';
import { fetchProducts } from '../api/apiService';
import ProductList from '../components/ProductList';
import Filter from '../components/Filter';
import generateUniqueId from '../utils/generateUniqueId';

const AllProductsPage = () => {
    const [products, setProducts] = useState([]);
    const [filter, setFilter] = useState({});

    useEffect(() => {
        const loadProducts = async () => {
            const data = await fetchProducts('AMZ', 'Laptop', 0, 10000); // Adjust as needed
            const productsWithIds = data.map(product => ({ ...product, id: generateUniqueId(product) }));
            setProducts(productsWithIds);
        };

        loadProducts();
    }, [filter]);

    const handleFilterChange = (newFilter) => {
        setFilter(prevFilter => ({ ...prevFilter, ...newFilter }));
    };

    return (
        <div>
            <Filter onFilterChange={handleFilterChange} />
            <ProductList products={products} />
        </div>
    );
};

export default AllProductsPage;
