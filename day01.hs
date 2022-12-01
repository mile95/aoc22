import Data.List

convertToInteger :: [[String]] -> [[Integer]]
convertToInteger [] = []
convertToInteger (x:xs) = map read x : convertToInteger xs

groupValues :: [String] -> [String] -> [[String]]
groupValues [] [] = []
groupValues [] y = y : groupValues [] []
groupValues (x:xs) [] = groupValues xs [x]  
groupValues (x:xs) y = 
  if x == "" then y : groupValues xs []
  else groupValues xs (x:y)

sumSubLists :: [[Integer]] -> [Integer]
sumSubLists [] = []
sumSubLists (x:xs) = sum x : sumSubLists xs

main = do
        contents <- readFile "input.txt"
        let rows = lines contents
        let groups = convertToInteger (groupValues rows [])
        let sums = sumSubLists groups
        print(maximum(sums))
        print(sum (take 3 (reverse (sort sums))))
