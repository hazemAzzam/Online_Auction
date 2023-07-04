# Online Auction Database System

This repository contains the documentation for an **Online Auction Database System**. The system allows members (buyers and sellers) to participate in the sale of items. The database system is designed to fulfill the following data requirements:

## Data Requirements

1. Members:
   - Each member is identified by a unique member number.
   - Member information includes:
     - E-mail address
     - Name
     - Password
     - Home address
     - Phone number

2. Buyer and Seller Information:
   - Members can be buyers or sellers.
   - Buyer information includes:
     - Shipping address
   - Seller information includes:
     - Bank account number
     - Routing number

3. Items:
   - Items are placed for sale by sellers.
   - Each item is identified by a unique item number assigned by the system.
   - Item information includes:
     - Item title
     - Description
     - Starting bid price
     - Bidding increment
     - Start date of the auction
     - End date of the auction

4. Item Categorization:
   - Items are categorized based on a fixed classification hierarchy.
   - Example: A modem may be classified as `COMPUTER → HARDWARE → MODEM`.

5. Bidding:
   - Buyers can place bids on items they are interested in.
   - Bids include:
     - Bid price
     - Time of bid

6. Auction Winner:
   - At the end of the auction, the bidder with the highest bid price is declared the winner.
   - A transaction between the buyer and seller may then proceed.

7. Feedback:
   - Members can record feedback regarding their completed transactions.
   - Feedback includes:
     - Rating of the other party participating in the transaction (scale: 1-10)
     - Comment


![EER Online_Aucation](https://github.com/hazemAzzam/Online_Auction/assets/61450444/2e324555-42f5-4306-ad85-e4f3860e6371)


## License

This project is licensed under the [MIT License](LICENSE).
