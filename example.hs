convertToInteger :: [String] -> [Integer]
convertToInteger = map read 

findIncreases :: [Integer] -> [Bool]
findIncreases [] = []
findIncreases [x] = []
findIncreases (x:xs) = (x < head xs) : findIncreases xs

sumThree :: [Integer] -> [Integer]
sumThree [] = []
sumThree [x] = []
sumThree (x:y:[]) = []
sumThree (x:y:xs) = (x + y + (head xs)) : sumThree (y:xs)


main = do
        contents <- readFile "input.txt"
        let rows = lines contents
        let ins = convertToInteger rows 
        let increases = filter (==True) (findIncreases ins)
        print(length increases)

        let increasesSumThree = filter (==True) (findIncreases (sumThree ins))
        print(length increasesSumThree)
        

