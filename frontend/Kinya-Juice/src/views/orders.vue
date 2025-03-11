<template>
  <div class="orders-container">
    <h1>Orders Management</h1>
    
    <!-- Create Order Form -->
    <div class="order-form-card">
      <h2>Create New Order</h2>
      <form @submit.prevent="createOrder">
        <div class="form-group">
          <label for="name">Name:</label>
          <input 
            type="text" 
            id="name" 
            v-model="newOrder.name" 
            required 
            placeholder="Enter product name"
          />
        </div>
        
        <div class="form-group">
          <label for="price">Price:</label>
          <input 
            type="number" 
            id="price" 
            v-model="newOrder.price" 
            step="0.01" 
            required 
            placeholder="Enter price"
          />
        </div>
        
        <div class="form-group">
          <label for="description">Description:</label>
          <textarea 
            id="description" 
            v-model="newOrder.description" 
            placeholder="Enter description"
          ></textarea>
        </div>
        
        <button type="submit" class="submit-button">Create Order</button>
      </form>
    </div>
    
    <!-- Orders List -->
    <div class="orders-list">
      <h2>All Orders</h2>
      <div v-if="loading">Loading orders...</div>
      <div v-else-if="error" class="error-message">{{ error }}</div>
      <div v-else-if="orders.length === 0" class="no-orders">No orders found.</div>
      
      <div v-else class="order-grid">
        <div v-for="order in orders" :key="order.id" class="order-card">
          <div class="order-header">
            <h3>{{ order.name }}</h3>
            <span class="order-price">${{ parseFloat(order.price).toFixed(2) }}</span>
          </div>
          <p class="order-description">{{ order.description }}</p>
          <div class="order-footer">
            <span class="order-id">Order #{{ order.id }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

// State
const orders = ref([]);
const loading = ref(true);
const error = ref(null);
const newOrder = ref({
  name: '',
  price: '',
  description: ''
});

// API URL - Update this to match your backend
const API_URL = 'http://localhost:5000/products'; // Change this to your actual API URL

// Fetch all orders
const fetchOrders = async () => {
  loading.value = true;
  error.value = null;
  
  try {
    const response = await axios.get(`${API_URL}/products`);
    orders.value = response.data;
  } catch (err) {
    console.error('Error fetching orders:', err);
    error.value = 'Failed to load orders. Please try again later.';
  } finally {
    loading.value = false;
  }
};

// Create a new order
const createOrder = async () => {
  try {
    // Convert price to number to ensure proper formatting
    const orderData = {
      ...newOrder.value,
      price: parseFloat(newOrder.value.price)
    };
    
    const response = await axios.post(`${API_URL}/products`, orderData);
    
    // Add the new order to the list
    orders.value.push(response.data);
    
    // Reset the form
    newOrder.value = {
      name: '',
      price: '',
      description: ''
    };
    
    // Show success message (you could implement a toast notification here)
    alert('Order created successfully!');
  } catch (err) {
    console.error('Error creating order:', err);
    error.value = 'Failed to create order. Please try again.';
  }
};

// Load orders when component mounts
onMounted(() => {
  fetchOrders();
});
</script>

<style scoped>
.orders-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h1, h2 {
  color: #333;
}

h1 {
  margin-bottom: 30px;
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 10px;
}

/* Form styling */
.order-form-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input, textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

textarea {
  min-height: 80px;
  resize: vertical;
}

.submit-button {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s;
}

.submit-button:hover {
  background: #3e8e41;
}

/* Orders list styling */
.order-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.order-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.order-header h3 {
  margin: 0;
  color: #333;
}

.order-price {
  font-weight: bold;
  color: #4CAF50;
  font-size: 18px;
}

.order-description {
  color: #666;
  flex-grow: 1;
  margin-bottom: 15px;
}

.order-footer {
  font-size: 14px;
  color: #888;
  border-top: 1px solid #f0f0f0;
  padding-top: 10px;
}

.error-message {
  color: #f44336;
  padding: 10px;
  background: #ffebee;
  border-radius: 4px;
  margin-bottom: 20px;
}

.no-orders {
  text-align: center;
  padding: 30px;
  color: #666;
  background: #f9f9f9;
  border-radius: 8px;
}
</style>