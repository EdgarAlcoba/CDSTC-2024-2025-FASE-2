import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:4040', // Base URL para todas las peticiones
});

export default api;