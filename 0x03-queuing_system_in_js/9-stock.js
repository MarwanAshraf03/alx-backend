import express from "express";
import redis from "redis";
import { promisify } from "util";
const client = redis.createClient({ url: "redis://localhost:6379" });
const app = express();
const listProducts = [
  { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];
function getItemById(id) {
  return listProducts.find((item) => item.Id === id);
}
// const setAsync = promisify(client.set).bind(client);
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
  //   setAsync(`item.${itemId}`, stock);
}
const getAsync = promisify(client.get).bind(client);
async function getCurrentReservedStockById(itemId) {
  //   return client.get(`item.${itemId}`);
  return await getAsync(`item.${itemId}`);
}

app.get("/list_products", (req, res) => {
  res.json(listProducts);
});
app.get("/list_products/:itemId", async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).json({ status: "Product not found" });
    return;
  }
  const reservedStock = await getCurrentReservedStockById(itemId);
  if (!reservedStock) {
    res.status(404).json({ status: "No stock found" });
    return;
  }
  item.initialAvailableQuantity = item.stock;
  item.currentQuantity = reservedStock;
  delete item.stock;
  res.json(item);
});
app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).json({ status: "Product not found" });
    return;
  }
  const reservedStock = await getCurrentReservedStockById(itemId);
  if (!reservedStock) {
    res.status(404).json({ status: "No Stock Available" });
    return;
  }
  if (reservedStock < 1) {
    res
      .status(403)
      .json({ status: "Not enough stock available", itemId: itemId });
    return;
  }
  reserveStockById(itemId, Number(reservedStock) - 1);
  res.json({ status: "Reservation confirmed", itemId: itemId });
});
app.listen(1245);
