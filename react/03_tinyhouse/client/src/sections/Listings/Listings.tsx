import React from "react";
import { server } from "../../lib/api";
import {
  DeleteListingData,
  DeleteListingVariables,
  ListingsData,
} from "./types";

const LISTINGS = `
query Listings {
  listings {
  id
  title
  image
  address
  price
  numOfGuests
  numOfBeds
  numOfBaths
  }
}
`;

const DELETE_LISTING = `
  mutation DeleteListing($id: ID!) {
    deleteListing(id: $id) {
      id
      title
    }
  }
`;

interface Props {
  title: string;
}

export const Listings = ({ title }: Props) => {
  const fetchListings = async () => {
    const { data } = await server.fetch<ListingsData>({
      query: LISTINGS,
    });
    console.log(data);
  };
  const deleteListing = async () => {
    const { data } = await server.fetch<
      DeleteListingData,
      DeleteListingVariables
    >({
      query: DELETE_LISTING,
      variables: {
        id: "612903a769b9d816f848d567",
      },
    });
    console.log(data);
  };

  return (
    <div>
      <h2>{title}</h2>
      <button onClick={fetchListings}>Get listings</button>
      <button onClick={deleteListing}>Delete a Listing</button>
    </div>
  );
};
