import qualified Data.Set as Set
import Data.List

halveSplit :: [a] -> ([a], [a])
halveSplit xs = splitAt l xs 
           where l = div (length xs) 2

findCommon :: Ord a => ([a], [a]) -> a
findCommon (a, b) = Set.elemAt 0 (Set.intersection (Set.fromList a) (Set.fromList b))

findCommonThree :: Ord a => ([a], [a], [a]) -> a
findCommonThree (a, b, c) = Set.elemAt 0 (Set.intersection (Set.fromList c) (Set.intersection (Set.fromList a) (Set.fromList b)))

computePrio :: String -> Int
computePrio [] = 0
computePrio (x:xs) = case elemIndex x (['a' .. 'z'] ++ ['A'..'Z']) of
                      Just n -> n + 1 + computePrio xs
                      Nothing -> 0 + computePrio xs

groupThree :: [String] -> [(String, String, String)]
groupThree [] = []
groupThree (x:y:z:xs) = (x,y,z) : groupThree xs

main = do
        contents <- readFile "input.txt"
        let rows = lines contents
        -- A
        let halves = map halveSplit rows
        let equals = map findCommon halves
        print(computePrio equals)
        -- B 
        let groups = groupThree rows
        let equalsThree = map findCommonThree groups
        print(computePrio equalsThree)
    
