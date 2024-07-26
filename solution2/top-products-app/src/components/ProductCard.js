// src/components/ProductCard.js
import React from 'react';

const ProductCard = ({ product }) => {
    return (
        <div className="product-card">
            <img src="/images/placeholder.jpg" alt={product.productName} />
            <h3>{product.productName}</h3>
            <p>Price: ${product.price}</p>
            <p>Rating: {product.rating}</p>
            <p>Discount: {product.discount}%</p>
            <p>Availability: {product.availability}</p>
        </div>
    );
};

export default ProductCard;
