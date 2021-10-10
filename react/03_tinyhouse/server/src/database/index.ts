import { MongoClient } from "mongodb";
import { Database } from "../lib/types";

const uri = `mongodb+srv://${process.env.DB_USER}:${process.env.DB_USER_PASSWORD}@${process.env.DB_CLUSTER}.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`;

export const connectDatabase = async (): Promise<Database> => {
  const client = new MongoClient(uri);
  await client.connect();
  const db = client.db("main");

  return {
    listings: db.collection("test_listings"),
  };
};
