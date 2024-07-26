// src/components/ProductDetail.js
import React from 'react';

const ProductDetail = ({ product }) => {
    return (
        <div className="product-detail">
            <img src="/images/placeholder.jpg" alt={product.productName} />
            <h1>{product.productName}</h1>
            <p>Price: ${product.price}</p>
            <p>Rating: {product.rating}</p>
            <p>Discount: {product.discount}%</p>
            <p>Availability: {product.availability}</p>
        </div>
    );
};

export default ProductDetail;
