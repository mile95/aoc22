computeScores :: [[String]] -> [Int]
computeScores [] = []
computeScores (xs:xss) = 
  if head xs == last xs then (3 + mapActionToValue(head xs)) : computeScores xss
  else if (head xs == "A") && (last xs == "B") then (6 + mapActionToValue(last xs)) : computeScores xss
  else if (head xs == "A") && (last xs == "C") then (0 + mapActionToValue(last xs)) : computeScores xss
  else if (head xs == "B") && (last xs == "A") then (0 + mapActionToValue(last xs)) : computeScores xss
  else if (head xs == "B") && (last xs == "C") then (6 + mapActionToValue(last xs)) : computeScores xss
  else if (head xs == "C") && (last xs == "A") then (6 + mapActionToValue(last xs)) : computeScores xss
  else if (head xs == "C") && (last xs == "B") then (0 + mapActionToValue(last xs)) : computeScores xss
  else undefined

myMap :: String -> String
myMap "X" = "A"
myMap "Y" = "B"
myMap "Z" = "C"
myMap x = x

mapAction :: String -> String -> String 
mapAction x y =
  if y == "B" then x 
  else if x == "A" && y == "A" then "C"
  else if x == "B" && y == "A" then "A"
  else if x == "C" && y == "A" then "B"
  else if x == "A" && y == "C" then "B"
  else if x == "B" && y == "C" then "C"
  else if x == "C" && y == "C" then "A"
  else undefined

mapActionToValue :: String -> Int
mapActionToValue "A" = 1
mapActionToValue "B" = 2
mapActionToValue "C" = 3

convertToSameFormat :: [[String]] -> [[String]]
convertToSameFormat [] = []
convertToSameFormat (x:xs) = map myMap x  : convertToSameFormat xs

convertActions :: [[String]] -> [[String]]
convertActions [] = []
convertActions (x:xs) = ((head x) : [mapAction (head x) (last x)]) : convertActions xs   

main = do
        contents <- readFile "input.txt"
        let rows = lines contents
        let formattedRows = convertToSameFormat (map words rows)
        let scoresA = computeScores(formattedRows)
        print(sum(scoresA))
        

        let scoresB = computeScores (convertActions formattedRows)
        print(sum scoresB)

