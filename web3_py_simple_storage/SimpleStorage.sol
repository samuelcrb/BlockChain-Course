//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SimpleStorage{

    uint favuriteNUmber;
    bool favoriteBool;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;

    mapping(string => uint256) public nameToFavoriteNumber;

    People public person = People({favoriteNumber: 2, name:"Sam"});
    
    function store(uint256 _favoriteNumber) public returns (uint256){
        favuriteNUmber = _favoriteNumber;
        return favuriteNUmber;
    }

    function retrieve() public view returns(uint256){
            return favuriteNUmber;
    }

    function  addPerson(string memory _name, uint256 _favoriteNumber) public{
            people.push( People(_favoriteNumber, _name));
            nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}