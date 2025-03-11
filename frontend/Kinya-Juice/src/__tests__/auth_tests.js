import { signup, login } from "../api";
import axios from "axios";
import MockAdapter from "axios-mock-adapter";

const mock = new MockAdapter(axios);

describe("Authentication API", () => {
  afterEach(() => {
    mock.reset();
  });

  test("signup should return success message", async () => {
    mock.onPost("http://127.0.0.1:5000/auth/signup").reply(201, {
      message: "User created successfully",
    });

    const response = await signup({ email: "test@example.com", password: "123456" });
    expect(response.message).toBe("User created successfully");
  });

  test("login should return access token", async () => {
    mock.onPost("http://127.0.0.1:5000/auth/login").reply(200, {
      access_token: "fake-jwt-token",
    });

    const response = await login("test@example.com", "123456");
    expect(response.access_token).toBe("fake-jwt-token");
  });
});
