// src/components/Filter.js
import React from 'react';

const Filter = ({ onFilterChange }) => {
    return (
        <div className="filter">
            <input type="text" placeholder="Search..." onChange={(e) => onFilterChange({ search: e.target.value })} />
            <select onChange={(e) => onFilterChange({ category: e.target.value })}>
                <option value="">Select Category</option>
                {/* Add more categories as needed */}
                <option value="Laptop">Laptop</option>
                <option value="Phone">Phone</option>
            </select>
            {/* Add more filters as needed */}
        </div>
    );
};

export default Filter;

