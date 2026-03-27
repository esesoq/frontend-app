// types.ts

// Define types for the frontend-app project

type User = {
  id: string;
  name: string;
  email: string;
  profilePicture: string;
}

type Product = {
  id: string;
  title: string;
  description: string;
  price: number;
  image: string;
  userId: string;
}

type ProductUpdate = {
  title?: string;
  description?: string;
  price?: number;
  image?: string;
}

type UserUpdate = {
  name?: string;
  email?: string;
  profilePicture?: string;
}

type Cart = {
  id: string;
  userId: string;
  products: Product[];
}

type Order = {
  id: string;
  userId: string;
  products: Product[];
  total: number;
  status: 'pending' | 'shipped' | 'delivered';
}

type NewOrder = {
  userId: string;
  products: Product[];
  total: number;
}