-- Optimize simple search
-- Creating an index
CREATE INDEX idx_name_first ON names(name(1));