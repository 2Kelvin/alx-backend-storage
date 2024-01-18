-- Optimize simple search
-- Creating an index
CREATE INDEX idx_name_first on names(name(1));