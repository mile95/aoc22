myParse :: [String] -> [[Integer]]
myParse [] = []
myParse (x:xs) = [a .. b] : myParse xs
                            where a = read (head (wordsWhen (=='-') x)) :: Integer
                                  b = read (last (wordsWhen (=='-') x)) :: Integer

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                  "" -> []
                  s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

findStrictOverlaps :: [[Integer]] -> Bool
findStrictOverlaps (x:y:[]) = ((head x) <= (head y) && (last x) >= (last y)) || ((head y) <= (head x) && (last y) >= (last x)) 

findAnyOverlaps :: [[Integer]] -> Bool
findAnyOverlaps (x:y:[]) = ((head x) <= (last y)) && ((last x) >= (head y))

main = do
        contents <- readFile "input.txt"
        let rows = lines contents
        let splitted = map (wordsWhen (==',')) rows 
        let ranges = map myParse splitted
        -- A
        let strictOverlaps = map findStrictOverlaps ranges
        print(length (filter (==True) strictOverlaps))
        -- B
        let anyOverlaps = map findAnyOverlaps ranges
        print(length (filter (==True) anyOverlaps))
