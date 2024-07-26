// src/pages/ProductDetailPage.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { fetchProducts } from '../api/apiService';
import ProductDetail from '../components/ProductDetail';
import generateUniqueId from '../utils/generateUniqueId';

const ProductDetailPage = () => {
    const { productId } = useParams();
    const [product, setProduct] = useState(null);

    useEffect(() => {
        const loadProduct = async () => {
            const data = await fetchProducts('AMZ', 'Laptop', 0, 10000); // Adjust as needed
            const foundProduct = data.find(p => generateUniqueId(p) === productId);
            setProduct(foundProduct);
        };

        loadProduct();
    }, [productId]);

    return (
        <div>
            {product ? <ProductDetail product={product} /> : <p>Loading...</p>}
        </div>
    );
};

export default ProductDetailPage;
