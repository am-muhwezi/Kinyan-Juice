import { render, screen } from "@testing-library/react";
import Orders from "../components/Orders"; // Adjust path
import axios from "axios";
import MockAdapter from "axios-mock-adapter";

const mock = new MockAdapter(axios);

test("renders orders list", async () => {
  mock.onGet("http://127.0.0.1:5000/products/products").reply(200, [
    { id: 1, name: "Juice 1" },
    { id: 2, name: "Juice 2" },
  ]);

  render(<Orders />);
  const orderItem = await screen.findByText(/Juice 1/i);
  expect(orderItem).toBeInTheDocument();
});
